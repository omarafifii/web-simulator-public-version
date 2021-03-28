import flask
import flask_praetorian
from . import guard
from flask import current_app as app
from .models import InitData, Project
import application.calculations as cal
from flasgger import swag_from
# from flask import session
# import datetime


@app.route('/')
def welcome():
    return 'Welcome to Marketeers Simulator API!'


@app.route('/api/', methods=['POST'])
def home():
    return {"Hello": "World Omar"}, 200


@app.route('/api/login', methods=['POST'])
@swag_from('../api_docs/login.yml')
def login():
    """
    Logs a user in by parsing a POST request containing user credentials and
    issuing a JWT token.
    .. example::
       $ curl http://localhost:5000/api/login -X POST -d "{\"username\":\"Omar\",\"password\":\"password\"}"
    """
    req = flask.request.get_json(force=True)
    username = req.get("username", None)
    password = req.get("password", None)
    user = guard.authenticate(username, password)
    ret = {"access_token": guard.encode_jwt_token(user)}
    return (flask.jsonify(ret), 200)


@app.route('/api/refresh', methods=['POST'])
@swag_from('../api_docs/refresh_login.yml')
def refresh():
    """
    Refreshes an existing JWT by creating a new one that is a copy of the old
    except that it has a refrehsed access expiration.
    .. example::
       $ curl http://localhost:5000/api/refresh -X GET \
         -H "Authorization: Bearer <your_token>"
    """
    print("refresh request")
    old_token = flask.request.get_data()
    new_token = guard.refresh_jwt_token(old_token)
    ret = {'access_token': new_token}
    return ret, 200


@app.route('/api/protected')
@flask_praetorian.auth_required
def protected():
    """
    A protected endpoint. The auth_required decorator will require a header
    containing a valid JWT
    .. example::
       $ curl http://localhost:5000/api/protected -X GET -H "Authorization: Bearer <your_token>"
    """
    return flask.jsonify(
        message="protected endpoint (allowed user {})".format(
            flask_praetorian.current_user().username
        )
    )


@app.route('/api/projects')
@flask_praetorian.auth_required
@swag_from('../api_docs/projects_user.yml')
def projects_user():
    """
    A protected endpoint. The auth_required decorator will require a header
    containing a valid JWT
    .. example::
       $ curl http://localhost:5000/api/projects -X GET -H "Authorization: Bearer <your_token>"
    """
    user_projects = flask_praetorian.current_user().projects
    return flask.jsonify(user_projects)


@app.route('/api/projects2/<int:project_id>')
@flask_praetorian.auth_required
@swag_from('../api_docs/get_project.yml')
def get_project(project_id):
    user_projects = flask_praetorian.current_user().projects
    if any(project.id == project_id for project in user_projects):
        # User has access to project
        data = InitData.query.filter_by(project_id=project_id).all()
        return flask.jsonify(data)
    else:
        # User does not have access to project
        return {'message': 'Unauthorized to view this project'}, 401

@app.route('/api/restore-defaults/<int:project_id>')
@app.route('/api/projects/<int:project_id>')
@flask_praetorian.auth_required
def get_project2(project_id):
    user_projects = flask_praetorian.current_user().projects
    if any(project.id == project_id for project in user_projects):
        # User has access to project
        # start = datetime.datetime.utcnow()
        
        project = Project.query.filter_by(id=project_id).first()
        data = cal.get_data(project_id)
        
        # Old method, does not calculate sop
        # ----------------------------------------
        # inactive_data = cal.get_inactive_sku(data)
        # data, active_list = cal.get_active_sku(data)
        # cal.calculate_value_part(data,project.msu,project.vsu)
        # data = cal.join_active_inactive_sku(data,inactive_data)
        # data_json = cal.convert_to_json(data)
    

        inactive_data = cal.get_inactive_sku(data)
        # time = datetime.datetime.utcnow() - start
        # print('1',time)
        data, active_list = cal.get_active_sku(data)
        # time = datetime.datetime.utcnow() - start
        # print('2',time)
        zero_price_level = cal.get_zero_price(active_list)
        # time = datetime.datetime.utcnow() - start
        # print('3',time)
        sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,active_list)
        # time = datetime.datetime.utcnow() - start
        # print('4',time)
        df_util = cal.get_init_utility_table(price,price_list,zero_price_level,data,project_id)
        # print('df_util',df_util)
        # time = datetime.datetime.utcnow() - start
        # print('5',time)
        sop = cal.calculate_sop_after_utility(df_util,sku)
        # time = datetime.datetime.utcnow() - start
        # print('6',time)
        cal.update_sop(data,sop)
        # time = datetime.datetime.utcnow() - start
        # print('7',time)

        
        # cal.update_volume_share(data)
        # cal.rebase_volume_share(data)

        cal.init_sop(data)
        # time = datetime.datetime.utcnow() - start
        # ('print8',time)
        
        cal.calculate_value_part(data,project.msu,project.vsu)
        # time = datetime.datetime.utcnow() - start
        # print('9',time)
        
        cal.calculate_financials(data)
        cal.calculate_financials_zero(inactive_data)

        data = cal.join_active_inactive_sku(data,inactive_data)

        
        # time = datetime.datetime.utcnow() - start
        # print('10',time)
        
        data_json = cal.convert_to_json(data)
        
        return flask.jsonify(data_json)
    else:
        # User does not have access to project
        return {'message': 'Unauthorized to view this project'}, 401 

@app.route('/api/projects/<int:project_id>/price-change', methods=['POST'])
@flask_praetorian.auth_required
@swag_from('../api_docs/price_change.yml')
def price_change(project_id):
    user_projects = flask_praetorian.current_user().projects
    if any(project.id == project_id for project in user_projects):
        # User has access to project
        project = Project.query.filter_by(id=project_id).first()
        req = flask.request.get_json(force=True)
        sku_id = req.get("sku-id", None)
        new_price = req.get("new-price", None)
        data_json = req.get("data", None)
        data = cal.df_load_json(data_json)
                
        cal.update_price(data,sku_id,new_price)

        # is_price_changed = cal.is_price_changed(data)
        # # print("is_price_changed: ", is_price_changed)
        # is_wd_changed = cal.is_wd_changed(data)
        # print("is_wd_changed: ", is_wd_changed)
        
        inactive_data = cal.get_inactive_sku(data)
        data, active_list = cal.get_active_sku(data)

        original_data = cal.get_data(project_id)
        original_inactive_data = cal.get_inactive_sku(original_data)
        original_inactive_list = cal.get_inactive_list(original_inactive_data)
        original_data, original_active_list = cal.get_active_sku(original_data)

        is_sku_introduced = cal.is_sku_introduced(original_data, data)
        # print("is_sku_introduced: {}".format(is_sku_introduced))
        
        if is_sku_introduced:
            zero_price_level = cal.get_zero_price(original_active_list)
            sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,original_active_list)
            df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
            sop = cal.calculate_sop_after_utility(df_util,sku)
            
            cal.update_sop(data,sop)
            cal.remove_inactive_sop(data, original_inactive_list)
            cal.update_sop_after_wd(data)
            
            cal.update_volume_share_using_base(data)
            cal.remove_inactive_volume_share(data, original_inactive_list)
            cal.rebase_volume_share_using_base(data)

            cal.update_old_sop(data, original_inactive_list)
            cal.update_old_volume_share(data, original_inactive_list)
            

        else:
            cal.default_old_sop(data)
            cal.default_old_volume_share(data)
            
        zero_price_level = cal.get_zero_price(active_list)
        sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,active_list)
        df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
        sop = cal.calculate_sop_after_utility(df_util,sku)
        cal.update_sop(data,sop)
        cal.update_sop_after_wd_without_rebase(data)
        
        cal.update_volume_share(data)
        cal.rebase_volume_share(data, original_active_list)

        cal.calculate_value_part(data,project.msu,project.vsu)

        cal.calculate_financials(data)
        cal.calculate_financials_zero(inactive_data)

        data = cal.join_active_inactive_sku(data,inactive_data)

        new_data = cal.convert_to_json(data)

        return flask.jsonify(new_data)
    else:
        # User does not have access to project
        return {'message': 'Unauthorized to view this project'}, 401


@app.route('/api/projects/<int:project_id>/wd-change', methods=['POST'])
@flask_praetorian.auth_required
def wd_change(project_id):
    user_projects = flask_praetorian.current_user().projects
    if any(project.id == project_id for project in user_projects):
        # User has access to project
        project = Project.query.filter_by(id=project_id).first()

        req = flask.request.get_json(force=True)
        sku_id = req.get("sku-id", None)
        new_wd = req.get("new-wd", None)
        data_json = req.get("data", None)
        
        data = cal.df_load_json(data_json)
        # print('old sop1', data.new_sop[0])
        cal.wd_change(data,sku_id,new_wd)
        # print('old sop2', data.new_sop[0])
        # is_price_changed = cal.is_price_changed(data)
        # # print("is_price_changed: ", is_price_changed)
        # is_wd_changed = cal.is_wd_changed(data)
        # print("is_wd_changed: ", is_wd_changed)
        
        inactive_data = cal.get_inactive_sku(data)
        data, active_list = cal.get_active_sku(data)

        original_data = cal.get_data(project_id)
        original_inactive_data = cal.get_inactive_sku(original_data)
        original_inactive_list = cal.get_inactive_list(original_inactive_data)
        original_data, original_active_list = cal.get_active_sku(original_data)

        is_sku_introduced = cal.is_sku_introduced(original_data, data)
        # print("is_sku_introduced: {}".format(is_sku_introduced))
                
        if is_sku_introduced:
            zero_price_level = cal.get_zero_price(original_active_list)
            sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,original_active_list)
            df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
            sop = cal.calculate_sop_after_utility(df_util,sku)

            cal.update_sop(data,sop)
            cal.remove_inactive_sop(data, original_inactive_list)
            cal.update_sop_after_wd(data)
            
            cal.update_volume_share_using_base(data)
            cal.remove_inactive_volume_share(data, original_inactive_list)
            cal.rebase_volume_share_using_base(data)
            
            cal.update_old_sop(data,original_inactive_list)
            cal.update_old_volume_share(data, original_inactive_list)
           

        else:
            cal.default_old_sop(data)
            cal.default_old_volume_share(data)
            
        zero_price_level = cal.get_zero_price(active_list)
        sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,active_list)
        df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
        sop = cal.calculate_sop_after_utility(df_util,sku)
        cal.update_sop(data,sop)
        # print('old sop', data.new_sop[0])
        # print('old  wd', data.base_wd[0])
        # print('new wd', data.new_wd[0])
        cal.update_sop_after_wd_without_rebase(data)
        # print('new sop', data.new_sop[0])
        cal.update_volume_share(data)
        cal.rebase_volume_share(data, original_active_list)

        cal.calculate_value_part(data,project.msu,project.vsu)

        cal.calculate_financials(data)
        cal.calculate_financials_zero(inactive_data)

        data = cal.join_active_inactive_sku(data,inactive_data)

        new_data = cal.convert_to_json(data)

        return flask.jsonify(new_data)
    else:
        # User does not have access to project
        return {'message': 'Unauthorized to view this project'}, 401

@app.route('/api/projects/<int:project_id>/introduction', methods=['POST'])
@flask_praetorian.auth_required
def introduction(project_id):
    user_projects = flask_praetorian.current_user().projects
    if any(project.id == project_id for project in user_projects):
        # User has access to project
        project = Project.query.filter_by(id=project_id).first()
        
        req = flask.request.get_json(force=True)
        sku_id = req.get("sku-id", None)
        is_active = req.get("is_active", None)
        data_json = req.get("data", None)
        
        data = cal.df_load_json(data_json)

        # is_price_changed = cal.is_price_changed(data)
        # print("is_price_changed: ", is_price_changed)
        # is_wd_changed = cal.is_wd_changed(data)
        # print("is_wd_changed: ", is_wd_changed)

        cal.activate_sku(data,sku_id,is_active)
        if not is_active:
            cal.remove_sop(data,sku_id)
        
        inactive_data = cal.get_inactive_sku(data)
        data, active_list = cal.get_active_sku(data)

        original_data = cal.get_data(project_id)
        original_inactive_data = cal.get_inactive_sku(original_data)
        original_inactive_list = cal.get_inactive_list(original_inactive_data)
        original_data, original_active_list = cal.get_active_sku(original_data)

        is_sku_introduced = cal.is_sku_introduced(original_data, data)
        # print("is_sku_introduced: {}".format(is_sku_introduced))
        
        if is_sku_introduced:
            zero_price_level = cal.get_zero_price(original_active_list)
            sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,original_active_list)
            df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
            sop = cal.calculate_sop_after_utility(df_util,sku)
            
            cal.update_sop(data,sop)
            cal.remove_inactive_sop(data, original_inactive_list)
            cal.update_sop_after_wd(data)
            
            cal.update_volume_share_using_base(data)
            cal.remove_inactive_volume_share(data, original_inactive_list)
            cal.rebase_volume_share_using_base(data)

            cal.update_old_sop(data, original_inactive_list)
            cal.update_old_volume_share(data, original_inactive_list)
            

        else:
            cal.default_old_sop(data)
            cal.default_old_volume_share(data)
            
        zero_price_level = cal.get_zero_price(active_list)
        sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,active_list)
        df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
        sop = cal.calculate_sop_after_utility(df_util,sku)
        cal.update_sop(data,sop)
        cal.update_sop_after_wd_without_rebase(data)
        
        cal.update_volume_share(data)
        cal.rebase_volume_share(data, original_active_list)

        cal.calculate_value_part(data,project.msu,project.vsu)

        cal.calculate_financials(data)
        cal.calculate_financials_zero(inactive_data)

        data = cal.join_active_inactive_sku(data,inactive_data)

        new_data = cal.convert_to_json(data)

        return flask.jsonify(new_data)
    else:
        # User does not have access to project
        return {'message': 'Unauthorized to view this project'}, 401


def calculate_new_data(data,project,project_id):
    inactive_data = cal.get_inactive_sku(data)
    data, active_list = cal.get_active_sku(data)

    original_data = cal.get_data(project_id)
    original_inactive_data = cal.get_inactive_sku(original_data)
    original_inactive_list = cal.get_inactive_list(original_inactive_data)
    original_data, original_active_list = cal.get_active_sku(original_data)

    is_sku_introduced = cal.is_sku_introduced(original_data, data)
    # print("is_sku_introduced: {}".format(is_sku_introduced))
    
    if is_sku_introduced:
        zero_price_level = cal.get_zero_price(original_active_list)
        sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,original_active_list)
        df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
        sop = cal.calculate_sop_after_utility(df_util,sku)
        
        cal.update_sop(data,sop)
        cal.remove_inactive_sop(data, original_inactive_list)
        cal.update_sop_after_wd_without_rebase(data)
        
        cal.update_volume_share_using_base(data)
        cal.remove_inactive_volume_share(data, original_inactive_list)
        cal.rebase_volume_share_using_base(data)

        cal.update_old_sop(data, original_inactive_list)
        cal.update_old_volume_share(data, original_inactive_list)
        

    else:
        cal.default_old_sop(data)
        cal.default_old_volume_share(data)
        
    zero_price_level = cal.get_zero_price(active_list)
    sku, price, price_list = cal.get_hbu_data(project.hbu_filename,project.start_price,active_list)
    df_util = cal.get_utility_table(price,price_list,zero_price_level,data,project_id)
    sop = cal.calculate_sop_after_utility(df_util,sku)
    cal.update_sop(data,sop)
    cal.update_sop_after_wd_without_rebase(data)
    
    cal.update_volume_share(data)
    cal.rebase_volume_share(data)

    cal.calculate_value_part(data,project.msu,project.vsu)

    data = cal.join_active_inactive_sku(data,inactive_data)

    new_data = cal.convert_to_json(data)

    return new_data