from bookDao import bookDAO

book1 = {
    'ISBN':2135451,
    'price':12,
    'author': 'jk',
    'title': 'blah'
}

book2 = {
    'ISBN':2135451,
    'price':999,
    'author': 'mary',
    'title': 'number 2'
}

#returnValue = bookDAO.create(book)
returnValue = bookDAO.getAll()
print(returnValue)
returnValue = bookDAO.findByID(book2['ISBN'])
print('Find by ID')
print(returnValue)
returnValue = bookDAO.update(book2)
print(returnValue)
print('Find by ID2')
returnValue = bookDAO.findByID(book2['ISBN'])
print(returnValue)
returnValue = bookDAO.delete(book2['ISBN'])
print(returnValue)
returnValue = bookDAO.getAll()
print(returnValue)