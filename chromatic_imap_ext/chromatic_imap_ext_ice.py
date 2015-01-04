# **********************************************************************
#
# Copyright (c) 2003-2011 ZeroC, Inc. All rights reserved.
#
# This copy of Ice is licensed to you under the terms described in the
# ICE_LICENSE file included in this distribution.
#
# **********************************************************************
#
# Ice version 3.4.2
#
# <auto-generated>
#
# Generated from file `chromatic_imap_ext.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

import Ice, IcePy, __builtin__

# Start of module chromatic_imap_ext
_M_chromatic_imap_ext = Ice.openModule('chromatic_imap_ext')
__name__ = 'chromatic_imap_ext'

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_node'):
    _M_chromatic_imap_ext._t_chromatic_node = IcePy.declareClass('::chromatic_imap_ext::chromatic_node')
    _M_chromatic_imap_ext._t_chromatic_nodePrx = IcePy.declareProxy('::chromatic_imap_ext::chromatic_node')

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_error_level'):
    _M_chromatic_imap_ext.chromatic_error_level = Ice.createTempClass()
    class chromatic_error_level(object):

        def __init__(self, val):
            assert(val >= 0 and val < 4)
            self.value = val

        def __str__(self):
            return self._names[self.value]

        __repr__ = __str__

        def __hash__(self):
            return self.value

        def __lt__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value < other.value;
            elif other == None:
                return False
            return NotImplemented

        def __le__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value <= other.value;
            elif other == None:
                return False
            return NotImplemented

        def __eq__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value == other.value;
            elif other == None:
                return False
            return NotImplemented

        def __ne__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value != other.value;
            elif other == None:
                return False
            return NotImplemented

        def __gt__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value > other.value;
            elif other == None:
                return False
            return NotImplemented

        def __ge__(self, other):
            if isinstance(other, _M_chromatic_imap_ext.chromatic_error_level):
                return self.value >= other.value;
            elif other == None:
                return False
            return NotImplemented

        _names = ('celCritical', 'celSystem', 'celSilent', 'celNoError')

    chromatic_error_level.celCritical = chromatic_error_level(0)
    chromatic_error_level.celSystem = chromatic_error_level(1)
    chromatic_error_level.celSilent = chromatic_error_level(2)
    chromatic_error_level.celNoError = chromatic_error_level(3)

    _M_chromatic_imap_ext._t_chromatic_error_level = IcePy.defineEnum('::chromatic_imap_ext::chromatic_error_level', chromatic_error_level, (), (chromatic_error_level.celCritical, chromatic_error_level.celSystem, chromatic_error_level.celSilent, chromatic_error_level.celNoError))

    _M_chromatic_imap_ext.chromatic_error_level = chromatic_error_level
    del chromatic_error_level

if not _M_chromatic_imap_ext.__dict__.has_key('_t_v_lines'):
    _M_chromatic_imap_ext._t_v_lines = IcePy.defineSequence('::chromatic_imap_ext::v_lines', (), IcePy._t_string)

if not _M_chromatic_imap_ext.__dict__.has_key('_t_chromatic_node_seq'):
    _M_chromatic_imap_ext._t_chromatic_node_seq = IcePy.defineSequence('::chromatic_imap_ext::chromatic_node_seq', (), _M_chromatic_imap_ext._t_chromatic_nodePrx)

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_file_exception'):
    _M_chromatic_imap_ext.chromatic_file_exception = Ice.createTempClass()
    class chromatic_file_exception(Ice.UserException):
        def __init__(self, reason='', cel=_M_chromatic_imap_ext.chromatic_error_level.celNoError):
            self.reason = reason
            self.cel = cel

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_name = 'chromatic_imap_ext::chromatic_file_exception'

    _M_chromatic_imap_ext._t_chromatic_file_exception = IcePy.defineException('::chromatic_imap_ext::chromatic_file_exception', chromatic_file_exception, (), None, (
        ('reason', (), IcePy._t_string),
        ('cel', (), _M_chromatic_imap_ext._t_chromatic_error_level)
    ))
    chromatic_file_exception._ice_type = _M_chromatic_imap_ext._t_chromatic_file_exception

    _M_chromatic_imap_ext.chromatic_file_exception = chromatic_file_exception
    del chromatic_file_exception

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_node'):
    _M_chromatic_imap_ext.chromatic_node = Ice.createTempClass()
    class chromatic_node(Ice.Object):
        def __init__(self):
            if __builtin__.type(self) == _M_chromatic_imap_ext.chromatic_node:
                raise RuntimeError('chromatic_imap_ext.chromatic_node is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::chromatic_imap_ext::chromatic_node')

        def ice_id(self, current=None):
            return '::chromatic_imap_ext::chromatic_node'

        def ice_staticId():
            return '::chromatic_imap_ext::chromatic_node'
        ice_staticId = staticmethod(ice_staticId)

        def name(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_chromatic_imap_ext._t_chromatic_node)

        __repr__ = __str__

    _M_chromatic_imap_ext.chromatic_nodePrx = Ice.createTempClass()
    class chromatic_nodePrx(Ice.ObjectPrx):

        def name(self, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_node._op_name.invoke(self, ((), _ctx))

        def begin_name(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_node._op_name.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_name(self, _r):
            return _M_chromatic_imap_ext.chromatic_node._op_name.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_nodePrx.ice_checkedCast(proxy, '::chromatic_imap_ext::chromatic_node', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_chromatic_imap_ext.chromatic_nodePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_chromatic_imap_ext._t_chromatic_nodePrx = IcePy.defineProxy('::chromatic_imap_ext::chromatic_node', chromatic_nodePrx)

    _M_chromatic_imap_ext._t_chromatic_node = IcePy.defineClass('::chromatic_imap_ext::chromatic_node', chromatic_node, (), True, None, (), ())
    chromatic_node._ice_type = _M_chromatic_imap_ext._t_chromatic_node

    chromatic_node._op_name = IcePy.Operation('name', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), IcePy._t_string, ())

    _M_chromatic_imap_ext.chromatic_node = chromatic_node
    del chromatic_node

    _M_chromatic_imap_ext.chromatic_nodePrx = chromatic_nodePrx
    del chromatic_nodePrx

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_file'):
    _M_chromatic_imap_ext.chromatic_file = Ice.createTempClass()
    class chromatic_file(_M_chromatic_imap_ext.chromatic_node):
        def __init__(self):
            if __builtin__.type(self) == _M_chromatic_imap_ext.chromatic_file:
                raise RuntimeError('chromatic_imap_ext.chromatic_file is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::chromatic_imap_ext::chromatic_file', '::chromatic_imap_ext::chromatic_node')

        def ice_id(self, current=None):
            return '::chromatic_imap_ext::chromatic_file'

        def ice_staticId():
            return '::chromatic_imap_ext::chromatic_file'
        ice_staticId = staticmethod(ice_staticId)

        def read(self, current=None):
            pass

        def write(self, text, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_chromatic_imap_ext._t_chromatic_file)

        __repr__ = __str__

    _M_chromatic_imap_ext.chromatic_filePrx = Ice.createTempClass()
    class chromatic_filePrx(_M_chromatic_imap_ext.chromatic_nodePrx):

        def read(self, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_file._op_read.invoke(self, ((), _ctx))

        def begin_read(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_file._op_read.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_read(self, _r):
            return _M_chromatic_imap_ext.chromatic_file._op_read.end(self, _r)

        def write(self, text, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_file._op_write.invoke(self, ((text, ), _ctx))

        def begin_write(self, text, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_file._op_write.begin(self, ((text, ), _response, _ex, _sent, _ctx))

        def end_write(self, _r):
            return _M_chromatic_imap_ext.chromatic_file._op_write.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_filePrx.ice_checkedCast(proxy, '::chromatic_imap_ext::chromatic_file', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_chromatic_imap_ext.chromatic_filePrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_chromatic_imap_ext._t_chromatic_filePrx = IcePy.defineProxy('::chromatic_imap_ext::chromatic_file', chromatic_filePrx)

    _M_chromatic_imap_ext._t_chromatic_file = IcePy.defineClass('::chromatic_imap_ext::chromatic_file', chromatic_file, (), True, None, (_M_chromatic_imap_ext._t_chromatic_node,), ())
    chromatic_file._ice_type = _M_chromatic_imap_ext._t_chromatic_file

    chromatic_file._op_read = IcePy.Operation('read', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_chromatic_imap_ext._t_v_lines, ())
    chromatic_file._op_write = IcePy.Operation('write', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (((), _M_chromatic_imap_ext._t_v_lines),), (), None, (_M_chromatic_imap_ext._t_chromatic_file_exception,))

    _M_chromatic_imap_ext.chromatic_file = chromatic_file
    del chromatic_file

    _M_chromatic_imap_ext.chromatic_filePrx = chromatic_filePrx
    del chromatic_filePrx

if not _M_chromatic_imap_ext.__dict__.has_key('chromatic_directory'):
    _M_chromatic_imap_ext.chromatic_directory = Ice.createTempClass()
    class chromatic_directory(_M_chromatic_imap_ext.chromatic_node):
        def __init__(self):
            if __builtin__.type(self) == _M_chromatic_imap_ext.chromatic_directory:
                raise RuntimeError('chromatic_imap_ext.chromatic_directory is an abstract class')

        def ice_ids(self, current=None):
            return ('::Ice::Object', '::chromatic_imap_ext::chromatic_directory', '::chromatic_imap_ext::chromatic_node')

        def ice_id(self, current=None):
            return '::chromatic_imap_ext::chromatic_directory'

        def ice_staticId():
            return '::chromatic_imap_ext::chromatic_directory'
        ice_staticId = staticmethod(ice_staticId)

        def list(self, current=None):
            pass

        def __str__(self):
            return IcePy.stringify(self, _M_chromatic_imap_ext._t_chromatic_directory)

        __repr__ = __str__

    _M_chromatic_imap_ext.chromatic_directoryPrx = Ice.createTempClass()
    class chromatic_directoryPrx(_M_chromatic_imap_ext.chromatic_nodePrx):

        def list(self, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_directory._op_list.invoke(self, ((), _ctx))

        def begin_list(self, _response=None, _ex=None, _sent=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_directory._op_list.begin(self, ((), _response, _ex, _sent, _ctx))

        def end_list(self, _r):
            return _M_chromatic_imap_ext.chromatic_directory._op_list.end(self, _r)

        def checkedCast(proxy, facetOrCtx=None, _ctx=None):
            return _M_chromatic_imap_ext.chromatic_directoryPrx.ice_checkedCast(proxy, '::chromatic_imap_ext::chromatic_directory', facetOrCtx, _ctx)
        checkedCast = staticmethod(checkedCast)

        def uncheckedCast(proxy, facet=None):
            return _M_chromatic_imap_ext.chromatic_directoryPrx.ice_uncheckedCast(proxy, facet)
        uncheckedCast = staticmethod(uncheckedCast)

    _M_chromatic_imap_ext._t_chromatic_directoryPrx = IcePy.defineProxy('::chromatic_imap_ext::chromatic_directory', chromatic_directoryPrx)

    _M_chromatic_imap_ext._t_chromatic_directory = IcePy.defineClass('::chromatic_imap_ext::chromatic_directory', chromatic_directory, (), True, None, (_M_chromatic_imap_ext._t_chromatic_node,), ())
    chromatic_directory._ice_type = _M_chromatic_imap_ext._t_chromatic_directory

    chromatic_directory._op_list = IcePy.Operation('list', Ice.OperationMode.Idempotent, Ice.OperationMode.Idempotent, False, (), (), (), _M_chromatic_imap_ext._t_chromatic_node_seq, ())

    _M_chromatic_imap_ext.chromatic_directory = chromatic_directory
    del chromatic_directory

    _M_chromatic_imap_ext.chromatic_directoryPrx = chromatic_directoryPrx
    del chromatic_directoryPrx

# End of module chromatic_imap_ext
