#!/usr/bin/env python

from robot.api import ExecutionResult, ResultVisitor


result = ExecutionResult('/var/local/robot/output.xml')

def suititerator(suites):
# Expect a list of TestSuite objects

    for s in suites:
        level = 1
        print 'Level %s: Suite Name:%s\n' % (level,s.name)
        if len(s.tests):
            for t in s.tests:
                print '       Test Name:%s Elapsed Time %s \n' % (t.name,t.elapsedtime)
        if len(s.suites):
            level = level +1
            for ss in s.suites:
                print 'Level %s:    Suite Name:%s\n' % (level,ss.name)
                if len(ss.tests):
                     for t in ss.tests:
                        print '           Test Name:%s Elapsed Time %s \n' % (t.name,t.elapsedtime)
                suititerator(ss.suites)



suititerator(result.suite.suites)
