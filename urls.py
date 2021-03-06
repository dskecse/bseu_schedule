import webapp2
from auth import AuthRequestInit, AuthRequestCallback
from events_calendar import ImportHandler, BatchInserter
from main import ScheduleApi, MainPage, HelpPage, AjaxProxy, EditPage, CommentHandler
from utils.maintenance import MaintenanceTask
from resolver import ResolveLink

SITE_URLS = [
    webapp2.Route(r'/', handler=MainPage),
    webapp2.Route(r'/edit', handler=EditPage),
    webapp2.Route(r'/auth', handler=AuthRequestInit),
    webapp2.Route(r'/calendar_auth', handler=AuthRequestCallback),
    webapp2.Route(r'/help', handler=HelpPage),
    webapp2.Route(r'/comment', handler=CommentHandler),
    webapp2.Route(r'/proxy', handler=AjaxProxy),
    webapp2.Route(r'/import', handler=ImportHandler),
    webapp2.Route(r'/schedule', handler=ScheduleApi),
    webapp2.Route(r'/scheduleapi', handler=ScheduleApi),  # legacy
    webapp2.Route(r'/link/<key>', handler=ResolveLink)
]

TASKS_URLS = [
    webapp2.Route(r'/task/create_events', handler=BatchInserter),
    webapp2.Route(r'/task/maintenance', handler=MaintenanceTask)
]