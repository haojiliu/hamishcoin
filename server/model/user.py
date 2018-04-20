class User:
  def __init__(self):
    self.id = uuid.uuid1()
    # TODO: this should not be stored as plain text in db
    self.private_key = 'some private key'

  def query_by_id(self, uid):
    return True

  def query_by_email(self, email):
    return True

  def query_by_phone(self, phone):
    return True

  def query_by_name(self, first_name, middle_name, last_name):
    return True
