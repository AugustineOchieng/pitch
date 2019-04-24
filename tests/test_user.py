import unittest
from app.models import User, Comments, Pitches
class UserModelTest(unittest.TestCase):
  def setUp(self):
    self.new_user = User(password='gus9999#')
  def test_password_setter(self):
    self.assertTrue(self.new_user.password_hash is not None)
  def test_no_access_password(self):
    with self.assertRaises(AttributeError):
      self.new_user.password
  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('gus9999#'))
class CommentsModelTest(unittest.TestCase):

    def setUp(self):
       self.new_comment = Comments(id=1, user_id = 2, comment = 'person of interest',pitch_id = '5',date_posted='2019-04-24')

    def test_comment_variables(self):
       self.assertEquals(self.new_comment.comment,'person of interest')
       self.assertEquals(self.new_comment.date_posted,'2019-04-24')
       self.assertEquals(self.new_comment.user_id, 2)
    def test_save_comment(self):

        self.assertTrue(len(Comments.query.all())>0)

