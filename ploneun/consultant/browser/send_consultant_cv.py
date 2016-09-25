from five import grok
from ploneun.consultant.content.consultant import IConsultant
import json
from Products.statusmessages.interfaces import IStatusMessage
from Products.CMFCore.utils import getToolByName
from zope.component import getAdapters
from collective.pdfexport.interfaces import IPDFEmailSource
from plone import api
from email.MIMEBase import MIMEBase
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email import Encoders
from zope.component import getMultiAdapter
import copy
import zipfile
try:
    from cStringIO import StringIO
except ImportError:
    from io import BytesIO as StringIO

import time
import os
from Products.CMFDefault.utils import checkEmailAddress
from Products.CMFDefault.exceptions import EmailAddressInvalid
from email.Header import Header
from plone import api

grok.templatedir('templates')

class send_consultant_cv(grok.View):
    grok.context(IConsultant)
    grok.require('zope2.View')
    
    def js(self):
        path = '/'.join(self.context.getPhysicalPath())+'/consultant_cv_recipients'
        recipients = self.context.unrestrictedTraverse(path).__call__()
        
        config = {
            'theme': 'facebook',
            'tokenDelimiter': '\n',
            'preventDuplicates': True,
            'prePopulate': json.loads(recipients),
        }
        
        return '''
            $(document).ready(function () {
                $('#email-recipients').tokenInput('%s', %s);
            })
        ''' % (
            self.context.absolute_url() + '/consultant_cv_recipients',
            json.dumps(config)
        )
        
    def submitted_recipients(self):
        if self.request.method == 'POST':
            config = {}
            if self.request.get('email-recipients'):
                config['prePopulate'] = [{'id': i, 'name': i} for i in self.request.get('email-recipients').split(',')]
                return json.dumps(config)
        return
    
    def form_submitted(self):
        if self.request.method == 'POST':
            statusmessages = IStatusMessage(self.request)
            if self.request.form:
                form = self.request.form
                mark = 0
                recipients = []
                subject = ''
                message = ''
                consultants = []
                
                cc_recipients = []
                
                if 'email-recipients' in form:
                    if not form['email-recipients']:
                        #statusmessages.add('Recipients is required', type='error')
                        mark += 1
                    recipients_raw = form['email-recipients'].replace('\r', ',').replace('\n', '').split(',')
                    recipients_raw2 = []
                    for rec in recipients_raw or []:
                        if validateaddress(rec.strip()):
                            recipients.append(rec.strip())
                    if not recipients:
                        #statusmessages.add('At least one recipient is required.', type='error')
                        mark += 1
                        return
                if 'email-subject' in form:
                    if not form['email-subject']:
                        #statusmessages.add('Subject is required', type='error')
                        mark += 1
                    subject = form['email-subject']
                if 'email-msg' in form:
                    if not form['email-msg']:
                        #statusmessages.add('Message is required', type='error')
                        mark += 1
                    message = form['email-msg']
                
                if 'email-cc' in form:
                    cc_raw = form['email-cc'].replace('\r', ',').replace('\n', '').split(',')
                    
                    cc_raw2 = []
                    if cc_raw:
                        for cc in cc_raw:
                            if validateaddress(cc.strip()):
                                cc_recipients.append(cc.strip())
                
                if mark > 0:
                    return
                else:
                    expanded_recipients = []
                    adapters = getAdapters((self.context,), IPDFEmailSource)
                    if recipients:
                        
                        #for recipient in recipients.split(','):
                        #    expanded = False
                        #    recipient = recipient.strip()
                            
                            
                        #    can_expand = self.can_expand(recipient)
                        #    if can_expand:
                        #        if can_expand == 'user':
                        #            expanded_recipients += self.get_user(recipient)
                        #        elif can_expand == 'group':
                        #            expanded_recipients += self.get_group(recipient)
                                
                            
                            
                        self.send_email(
                            recipients=list(set(recipients)),
                            subject=subject,
                            message=message,
                            cc=cc_recipients
                        )
                                
                                
    def send_email(self, recipients, subject, message, cc):
        portal_url = getToolByName(self.context, 'portal_url')
        portal_catalog = getToolByName(self.context, 'portal_catalog')
        portal_state = getMultiAdapter((self.context, self.request), name=u"plone_portal_state")
        portal = portal_url.getPortalObject()
        mFrom = portal.getProperty('email_from_address')
        statusmessages = IStatusMessage(self.request)        
        mailhost = self.context.MailHost
        from_address = api.user.get_current().getProperty('email')
        msg = MIMEMultipart()
        msg['Subject'] = subject
        
        msg['From'] = '%s <%s>' % (portal_state.portal_title(), mFrom)
        
        htmlPart = MIMEText(message, 'plain', 'utf-8')
        msg.attach(htmlPart)
        zipped = []
        timestr = time.strftime("%Y%m%d-%H%M%S")
        context = self.context
        consultant_uid = context.UID()
        if consultant_uid:
            
            brains = portal_catalog.unrestrictedSearchResults(portal_type='ploneun.consultant.consultant', UID=consultant_uid)
            uploaded_files = []
            for brain in brains:
                brains2 = portal_catalog.unrestrictedSearchResults(path={'query':brain.getPath(), 'depth':1}, portal_type='File')
                for brain2 in brains2:
                    obj2 = brain2._unrestrictedGetObject()
                    
                    if obj2.getFile():
                        uploaded_files.append({'file': obj2.getFile().getBlob().open().name, 'filename':obj2.getFile().filename})
            
            if uploaded_files:
                
                zf = zipfile.ZipFile("/tmp/%s.zip" % timestr, "w", zipfile.ZIP_DEFLATED)
                for uf in uploaded_files:
                    zf.write(uf['file'], uf['filename'])
                zf.close()
                attachment = MIMEBase('application', 'zip')
                attachment.set_payload(open(zf.filename).read())
                open(zf.filename).close()
                Encoders.encode_base64(attachment)
                attachment.add_header('Content-Disposition', 'attachment',
                               filename='consultant-cvs' + '.zip')
                msg.attach(attachment)
                
                
        msg['To'] = ','.join(recipients)
        if cc:
            msg['cc'] = ','.join(cc)
        
        mailhost.send(msg.as_string())
        
        
        #for recipient in recipients:
        #    # skip broken recipients
        #    if not recipient:
        #        continue
        #    if '@' not in recipient:
        #        continue

        #    del msg['To']
        #    msg['To'] = recipient
        #    mailhost.send(msg.as_string())
        
        
        for f in os.listdir('/tmp/'):
            if timestr+'.zip' == f:
                os.remove('/tmp/'+f)
        
        statusmessages.add('Emails sent')
        self.request.response.redirect(self.context.absolute_url())
    
    
    
    def can_expand(self, value):
        if value.startswith('UserID:'):
            return 'user'
        elif value.startswith('Group'):
            return 'group'
        return ''
        
        
    def get_user(self, value):
        username = value.replace('UserID:','')
        user = api.user.get(username)
        if not user:
            return []
        fullname = user.getProperty('fullname')
        email = user.getProperty('email')
        if not email:
            return []
        value = '%s <%s>' % (fullname, email)
        return [value]
    
    def get_group(self, value):
        values = []
        groupid = value.replace('Group:', '')
        users = api.user.get_users(groupname=groupid)
        for user in users:
            values.append('%s <%s>' % (
                user.getProperty('fullname'),
                user.getProperty('email')
            ))
        return list(set(values))
    
    def error_message(self, form_name=''):
        results = {'status':False, 'msg':'', 'type':''}
        if self.request.method == 'POST':
            if form_name == 'email-recipients':
                
                recipients = self.request.form[form_name]
                if not recipients:
                    results['status'] = True
                    results['msg'] = 'At least one recipient is required.'
                    results['type'] = 'Error'
                recipients = recipients.replace('\r', ',').replace('\n', '').split(',')
                for rec in recipients or []:
                    if not validateaddress(rec.strip()):
                        results['status'] = True
                        results['msg'] = 'One of the email addresses is invalid.'
                        results['type'] = 'Error'
                        break
            
            if form_name == 'email-cc':
                data = self.request.form[form_name]
                if data:
                    data = data.replace('\r', ',').replace('\n', '').split(',')
                    for dat in data or []:
                        if not validateaddress(dat.strip()):
                            results['status'] = True
                            results['msg'] = 'One of the email addresses is invalid.'
                            results['type'] = 'Error'
                            break
            
            if form_name == 'email-subject':
                if not self.request.form[form_name]:
                    results['status'] = True
                    results['msg'] = 'Please provide subject for this email.'
                    results['type'] = 'Error'
                    
            if form_name == 'email-msg':
                if not self.request.form[form_name]:
                    results['status'] = True
                    results['msg'] = 'Please provide message for this email.'
                    results['type'] = 'Error'
                    
            
            if form_name == 'consultants_name':
                if not 'consultants_name' in self.request.form:
                    results['status'] = True
                    results['msg'] = 'Please select at least one consultant.'
                    results['type'] = 'Error'
        return results
    
    def form_values(self, form_name=''):
        form = self.request.form
        if form:
            if form.has_key(form_name):
                return form[form_name]
    
    def isChecked(self, uid=''):
        form = self.request.form
        if self.request.method == 'POST':
            if 'consultants_name' in form:
                
                if uid in form['consultants_name']:
                    return True
                return False
    
    
    
def validateaddress(value):
    try:
        checkEmailAddress(value)
    except EmailAddressInvalid:
        return False
    return True