# Copyright (c) 2010 gocept gmbh & co. kg
# See also LICENSE.txt

from zeit.cms.i18n import MessageFactory as _
import zope.interface
import zope.schema


class IAuthor(zope.interface.Interface):

    title = zope.schema.TextLine(title=_('Title'), required=False)
    firstname = zope.schema.TextLine(title=_('Firstname'))
    lastname = zope.schema.TextLine(title=_('Lastname'))
    vgwortid = zope.schema.TextLine(title=_('VG-Wort ID'))
