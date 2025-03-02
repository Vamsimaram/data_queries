
# author: Alex Brodsky
# date: Aug 30, 2022
# --------------------
import sys
import os
import json
import copy
from collections import OrderedDict

def load_json(path):
	with open(path, 'r') as f:
		data = json.load(f)
	return data

def recEqual(d1,d2):
    return(d1==d2)

def generateReport(answers, correct_answers):
    dbs = [db for db in correct_answers]
    # print("dbs=",dbs)
    queries = [ q for q in correct_answers[dbs[0]]]
    # print("queries=", queries)
    noQueries = len(queries)

    def perDBreport(q):
        return ([ { "query": q,
                    "db": db,
                    "correct": recEqual(answers[db][q],correct_answers[db][q])
                 }
                 for db in dbs
        ])

    perQueryReport = [ {
            "query": q,
            "correct": all([ recEqual(answers[db][q],correct_answers[db][q])
                            for db in dbs
            ]),
            "perDBreport": perDBreport(q)
            }
            for q in queries
    ]
    return { "correct_queries": len([qRep for qRep in perQueryReport if qRep["correct"]]),
             "outOf": noQueries,
             "perQueryReport": perQueryReport
    }

correct_answers = load_json("../testDBs/correct_answers.json")
answers = load_json("answers.json")
report = generateReport(answers,correct_answers)
with open("report.json", "w") as f:
    f.write(json.dumps(report))
