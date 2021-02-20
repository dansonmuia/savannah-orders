from flask import jsonify, request


MAX_ITEMS_PER_PAGE = 50


def paginate(model_query, items_per_page=MAX_ITEMS_PER_PAGE):
    page = request.args.get('page', 1, int)
    try:
        items_per_page = min(int(items_per_page), MAX_ITEMS_PER_PAGE)
    except (TypeError, ValueError):
        items_per_page = MAX_ITEMS_PER_PAGE

    try:
        page = int(page)
    except (TypeError, ValueError):
        page = 1

    pagination = model_query.paginate(page, per_page=items_per_page, error_out=False)

    return pagination


def jsonify_pagination(pagination, status_code=200):
    json_items = [item.to_json() for item in pagination.items]
    json_data = {'items': json_items,
                 'page': pagination.page,
                 'total_pages': pagination.pages,
                 'items_per_page': pagination.per_page,
                 'total_items': pagination.total,
                 'has_prev': pagination.has_prev,
                 'has_next': pagination.has_next,
                 'next_num': pagination.next_num,
                 'prev_num': pagination.prev_num,
                 }

    json_response = jsonify(json_data)
    json_response.status_code = status_code
    return json_response
