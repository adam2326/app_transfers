import datetime
import webapp2

class MainPage(webapp2.RequestHandler):
	def get(self):
		message = "<p>The time is: </p>" % datetime.datetime.now()
		self.response.out.write(message)

application = webapp2.WSGIApplication([('/', MainPage)], debug=True)
