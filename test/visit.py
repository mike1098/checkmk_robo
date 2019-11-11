#!/usr/bin/env python


from robot.api import ExecutionResult, ResultVisitor

outdir='/var/local/robot'

result = ExecutionResult('%s/output.xml' % outdir)
result.configure(stat_config={'suite_stat_level': 2,
                              'tag_stat_combine': 'tagANDanother'})

class TestMetrics(ResultVisitor):

    def visit_test(self,test):
        print "Test Name: " + str(test.name)
        print "Test Status: " + str(test.status)
        print "Test Starttime: " + str(test.starttime)
        print "Test Endtime: " + " " + str(test.endtime)
        print "Test Elapsedtime (Sec): " + " " + str(test.elapsedtime/float(1000))

class Child_Suite_Visitor(ResultVisitor):
    def visit_child_suite(self, childsuite):
        print 'Child Suite Name: %s\n' % childsuite.name

class SuitMetrics(ResultVisitor):
    def visit_suite(self, suite):
        print 'Suite Name: %s\n' % suite.name
        child_suite=suite.suites
        print type(child_suite)
        #child_suite.visit(Child_Suite_Visitor)

result.visit(SuitMetrics())
#result.visit(TestMetrics())
