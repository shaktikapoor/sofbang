
#from java.io import FileInputStream 
from oracle.fabric.blocks.folder import Folder
from oracle.fabric.management.folder import FolderManager
from javax.management import MBeanException 
from java.lang.reflect import InvocationTargetException


"""
-------------------------------------------------------------------------------
Partition Management operations
-------------------------------------------------------------------------------
"""
# This command creates the partition
#
# @partitionName The name of the partition
def sca_createPartition(partitionName):
   foldermbean = sca_getFolderMBean();
   print 'partitionName =', partitionName
   params = jarray.array([partitionName],java.lang.Object)
   signature = jarray.array(['java.lang.String'],java.lang.String)
   try:
#       print 'Calling folder mbean to create partition...'
       mbs.invoke(foldermbean, "create", params, signature)
#       print 'Partition was successfully created.'
       print WLSTMessageBundle.getStringNoArg(WLSTMessageID.FOLDER_CREATE_SUCCESS)
   except MBeanException, mbeanEx:
       if mbeanEx.getCause() != None and isinstance(mbeanEx.getCause(), InvocationTargetException) and mbeanEx.getCause().getCause() != None:
#           print mbeanEx.getCause().getCause()
           print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, mbeanEx.getCause().getCause().getMessage())
       else: 
           print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, mbeanEx)
   except Exception, detail:
       print 'Exception:', detail
#       print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, detail)

def sca_checkWLSConnection2():
 if (mbs is None):
#		raise UserWarning, "No connection to a Weblogic server exists. This operation can be executed only in the online mode."
		raise UserWarning, WLSTMessageBundle.getStringNoArg(WLSTMessageID.MBEAN_NO_CONNECTION)

def sca_getFolderMBean():
    sca_checkWLSConnection2()
#    serverMbName = ObjectName('oracle.soa.config:j2eeType=CompositeStore,name=online,*')
    serverMbName = ObjectName('*:j2eeType=FolderLifecycleConfig,*')
    beans = mbs.queryMBeans(serverMbName, None)
    if beans != None and java.util.Iterator.hasNext(beans.iterator())==true:
        return beans.iterator().next().getObjectName()
    else:
#        raise UserWarning, 'Cannot find folder lifecycle mbean on this server.'
        raise UserWarning, WLSTMessageBundle.getStringNoArg(WLSTMessageID.FOLDER_MBEAN_NOT_FOUND)

# This command deletes the partition
#
# @partitionName The name of the partition
def sca_deletePartition(partitionName):
   foldermbean = sca_getFolderMBean();
   print 'partitionName =', partitionName
   params = jarray.array([partitionName],java.lang.Object)
   signature = jarray.array(['java.lang.String'],java.lang.String)
   try:
#       print 'Calling folder mbean to destroy partition...'
       mbs.invoke(foldermbean, "destroy", params, signature)
#       print 'Partition was successfully destroyed.'
       print WLSTMessageBundle.getStringNoArg(WLSTMessageID.FOLDEDR_DESTROY_SUCCESS)
   except MBeanException, mbeanEx:
       if mbeanEx.getCause() != None and isinstance(mbeanEx.getCause(), InvocationTargetException) and mbeanEx.getCause().getCause() != None:
#           print mbeanEx.getCause().getCause()
           print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, mbeanEx.getCause().getCause().getMessage())
       else:
           print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, mbeanEx)
   except Exception, detail:
#       print 'Exception:', detail
       print WLSTMessageBundle.getStringWithOneArg(WLSTMessageID.MSG_EXCEPTION, detail)
	   
	   
def main():
	connect(<<soaUserName>>,<<soaPassword>>,<<t3://SOA Server HostName:SOA Server Port>>)	
	sca_createPartition("CRMSYNC");
	sca_createPartition("CRMASYNC");
	sca_createPartition("MEDIATOR");
	sca_createPartition("UTILITIES");
	disconnect()
	print 'successfully created the partions'
 
main()
