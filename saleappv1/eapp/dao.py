from eapp.models import Category,Product

def load_categories():
    return Category.query.order_by('id').all()

    query=Product.query
    if kw:
        query=query.filter(Product.name.contains(kw))

    if cate_id:
        query=query.filter(Product.category_id==int(cate_id))