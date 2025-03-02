def imply(lhs,rhs):
    return((not lhs) or rhs)

def queries(univDB):
    tables = univDB["tables"]
    department = tables["department"]
    course = tables["course"]
    prereq = tables["prereq"]
# class may be a reserved word - check
    class_ = tables["class"]
    faculty = tables["faculty"]
    student = tables["student"]
    enrollment = tables["enrollment"]
    transcript = tables["transcript"]

# boolean queries
# replace placeholders (True) with a Boolean expression that correctly answers each corresponding query

    boolQuery_a = True

    boolQuery_b = True

    boolQuery_c = True

    boolQuery_d = True

    boolQuery_e = True

    boolQuery_f = True

    boolQuery_g = True

    boolQuery_h = True

    boolQuery_i = True

    boolQuery_j = True

    boolQuery_k = True

    boolQuery_l = True

    # data queries
    # replace the placeholder answers with Python comprehensions that correctly answer each corresponding query

    dataQuery_a = [ {
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_a.sort(key=lambda t: t["ssn"])

    dataQuery_b =  [{
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_b.sort(key=lambda t: t["ssn"])

    dataQuery_c =  [{
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_c.sort(key=lambda t: t["ssn"])

    dataQuery_d =  [{
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_d.sort(key=lambda t: t["ssn"])

    dataQuery_e = [ {
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_e.sort(key=lambda t: t["ssn"])

    dataQuery_f = [ {
        "dcode": "MTH",
        "cno": 105
    }]
    dataQuery_f.sort(key=lambda t: (t["dcode"],t["cno"]))

    dataQuery_g = [{
        "dcode": "MTH",
        "cno": 105
      }
    ]
    dataQuery_g.sort(key=lambda t: (t["dcode"],t["cno"]))

    dataQuery_h = [{
        "class": 21,
        "dcode": "CS",
        "cno": 330,
        "instr": 25
      }]
    dataQuery_h.sort(key=lambda t: t["class"])

    dataQuery_i = [ {
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_i.sort(key=lambda t: t["ssn"])

    dataQuery_j = [ {
        "ssn": 5,
        "name": "Jackson",
        "major": "MTH",
        "status": "active"
    }]
    dataQuery_j.sort(key=lambda t: t["ssn"])

    return({
        "boolQuery_a": boolQuery_a,
        "boolQuery_b": boolQuery_b,
        "boolQuery_c": boolQuery_c,
        "boolQuery_d": boolQuery_d,
        "boolQuery_e": boolQuery_e,
        "boolQuery_f": boolQuery_f,
        "boolQuery_g": boolQuery_g,
        "boolQuery_h": boolQuery_h,
        "boolQuery_i": boolQuery_i,
        "boolQuery_j": boolQuery_j,
        "boolQuery_k": boolQuery_k,
        "boolQuery_l": boolQuery_l,
        "dataQuery_a": dataQuery_a,
        "dataQuery_b": dataQuery_b,
        "dataQuery_c": dataQuery_c,
        "dataQuery_d": dataQuery_d,
        "dataQuery_e": dataQuery_e,
        "dataQuery_f": dataQuery_f,
        "dataQuery_g": dataQuery_g,
        "dataQuery_h": dataQuery_h,
        "dataQuery_i": dataQuery_i,
        "dataQuery_j": dataQuery_j
    })
