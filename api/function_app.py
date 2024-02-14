import azure.functions as func
import logging
import json

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.function_name(name="GetProducts")
@app.route(route="gettodo")
@app.sql_input(arg_name="products",
                        command_text="select [Id], [order], [title], [url], [completed] from dbo.ToDo",
                        command_type="Text",
                        connection_string_setting="SqlConnectionString")
#testing the commit

def get_products(req: func.HttpRequest, products: func.SqlRowList) -> func.HttpResponse:
    rows = list(map(lambda r: json.loads(r.to_json()), products))

    return func.HttpResponse(
        json.dumps(rows),
        status_code=200,
        mimetype="application/json"
    )
