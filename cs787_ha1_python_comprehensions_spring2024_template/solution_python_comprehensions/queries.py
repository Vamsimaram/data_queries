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

    #The student with ssn = 82 has taken the course “CS 530” (must be in Transcipts) 
    boolQuery_a = any(
                    t['dcode'] == 'CS' and 
                    str(t['cno']) == '530' and 
                    str(t['ssn']) == '82' and 
                    t['grade'] not in ['F', 'W', 'I'] 
                    for t in transcript
                )

    #A student named “John  Smith” has taken the course “CS 530” (must be in Transcipts).  
    boolQuery_b = any(
                    s['name'].strip() == 'John Smith' and
                    any(
                        t['dcode'] == 'CS' and 
                        str(t['cno']) == '530' and 
                        t['ssn'] == s['ssn'] and 
                        t['grade'] not in ['F', 'W', 'I']
                        for t in transcript
                    )
                    for s in student
                )

    #All students named “John  Smith” has taken the course “CS 530” (must be in Transcipts) 
    boolQuery_c = all(
                    any(
                        t['dcode'] == 'CS' and 
                        str(t['cno']) == '530' and 
                        t['ssn'] == s['ssn'] and 
                        t['grade'] not in ['F', 'W', 'I']
                        for t in transcript
                    )
                    for s in student
                    if s['name'].strip() == 'John Smith'
                )
    #The student with ssn = 82  has satisfied all prerequisites for each class she is enrolled in.  
    boolQuery_d = (
                bool(enrollment) and bool(class_) and bool(transcript) and  
                all(
                    all(
                        any(
                            t['dcode'] == p['pcode'] and
                            t['cno'] == p['pno'] and
                            t['ssn'] == 82 and
                            t['grade'] not in ['F', 'W', 'I']  
                            for t in transcript
                        ) 
                        for p in prereq
                        if p['dcode'] == c['dcode'] and p['cno'] == c['cno']
                    ) if any(p['dcode'] == c['dcode'] and p['cno'] == c['cno'] for p in prereq)  
                    else True  
                    for c in class_
                    for e in enrollment
                    if e['ssn'] == 82 and e['class'] == c['class']
                )
            )

    #Every student has satisfied all prerequisites each class she is enrolled in.
    boolQuery_e = all(
                    all(
                        all(
                            any(
                                t['dcode'] == p['pcode'] and
                                t['cno'] == p['pno'] and
                                t['ssn'] == s['ssn'] and
                                t['grade'] not in ['F', 'W', 'I']
                                for t in transcript
                            )
                            for p in prereq
                            if p['dcode'] == c['dcode'] and p['cno'] == c['cno']
                        ) if any(p['dcode'] == c['dcode'] and p['cno'] == c['cno'] for p in prereq) else True
                        for e in enrollment
                        for c in class_
                        if e['ssn'] == s['ssn'] and e['class'] == c['class']
                    )
                    for s in student
                )

    # Checking if every CS major has satisfied all prerequisites for enrolled classes
    boolQuery_f = all(
        all(
            all(
                any(
                    t['dcode'] == p['pcode'] and  
                    t['cno'] == p['pno'] and  
                    t['ssn'] == s['ssn'] and  
                    t['grade'] not in ['F', 'W', 'I']  
                    for t in transcript
                )
                for p in prereq
                if p['dcode'] == c['dcode'] and p['cno'] == c['cno']  
            ) if any(p['dcode'] == c['dcode'] and p['cno'] == c['cno'] for p in prereq) else True  

            for c in class_  
            if any(e['ssn'] == s['ssn'] and e['class'] == c['class'] for e in enrollment)  
        )
        for s in student
        if s['major'] == 'CS'  
    )


    #A student named “John  Smith” is enrolled in a class for which he did satisfied all prerequisites. 
    boolQuery_g = any(
                    s['name'] == 'John Smith' and
                    any(
                        all(
                            any(
                                t['dcode'] == p['pcode'] and
                                t['cno'] == p['pno'] and
                                t['ssn'] == s['ssn'] and
                                t['grade'] not in ['F', 'W', 'I']
                                for t in transcript
                            )
                            for p in prereq
                            if p['dcode'] == c['dcode'] and p['cno'] == c['cno']
                        ) if any(p['dcode'] == c['dcode'] and p['cno'] == c['cno'] for p in prereq) else True
                        for e in enrollment
                        for c in class_
                        if e['ssn'] == s['ssn'] and e['class'] == c['class']
                    )
                    for s in student
                )

    #Some courses do not have prerequisites
    boolQuery_h = any(
                    not any(
                        p['dcode'] == c['dcode'] and p['cno'] == c['cno']
                        for p in prereq
                    )
                    for c in course
                )

    #All classes offered this semester have prerequisites. 
    boolQuery_i = all(
                    any(
                        p['dcode'] == c['dcode'] and p['cno'] == c['cno']
                        for p in prereq
                    )
                    for c in class_
                )

    # Some students received only grades “A” or “B” in every course they have taken (must appear in Transcripts)
    boolQuery_j = any(
        (
            all(t["grade"] in ["A", "B"] for t in transcript if t["ssn"] == s["ssn"])  
            if any(t["ssn"] == s["ssn"] for t in transcript)  
            else True  
        )
        for s in student
    )


    #All students currently enrolled in classes taught by professor Brodsky (i.e., the name is "Brodsky" in faculty), major in “CS” 
    boolQuery_k = all(
                    s['major'] == 'CS'
                    for s in student
                    if any(
                        e['ssn'] == s['ssn'] and
                        any(
                            c['class'] == e['class'] and
                            any(
                                f['ssn'] == c['instr'] and f['name'] == 'Brodsky'
                                for f in faculty
                            )
                            for c in class_
                        )
                        for e in enrollment
                    )
                )

    #Some students who are currently enrolled in classes taught by professor Brodsky major in “CS” 
    boolQuery_l = any(
                    s['major'] == 'CS' and
                    any(
                        e['ssn'] == s['ssn'] and
                        any(
                            c['class'] == e['class'] and
                            any(
                                f['ssn'] == c['instr'] and f['name'] == 'Brodsky'
                                for f in faculty
                            )
                            for c in class_
                        )
                        for e in enrollment
                    )
                    for s in student
                )

    # data queries
    # replace the placeholder answers with Python comprehensions that correctly answer each corresponding query

    # Students who have taken CS 530
    dataQuery_a = sorted(
        [
            s for s in student
            if any(t["dcode"] == "CS" and t["cno"] == 530 and t["ssn"] == s["ssn"] for t in transcript)
        ],
        key=lambda t: t["ssn"]
    )

    # Students named "John" who have taken CS 530
    dataQuery_b = sorted(
        [
            s for s in student
            if s["name"] == "John" and any(t["dcode"] == "CS" and t["cno"] == 530 and t["ssn"] == s["ssn"] for t in transcript)
        ],
        key=lambda t: t["ssn"]
    )

    # Create a dictionary to track which students have passed which courses
    student_passed_courses = {}
    for entry in transcript:
        if entry["grade"] in ["A", "B", "C"]:  
            student_passed_courses.setdefault(entry["ssn"], set()).add((entry["dcode"], entry["cno"]))

    # Create a dictionary to track prerequisites for each course
    class_prereqs = {}
    for prereq_entry in prereq:
        class_prereqs.setdefault((prereq_entry["dcode"], prereq_entry["cno"]), set()).add(
            (prereq_entry["pcode"], prereq_entry["pno"])
        )

    # Identify students who have satisfied all prerequisites for their enrolled classes
    dataQuery_c = sorted(
        [
            s for s in student
            if all(
                (enrolled_class := next((c for c in class_ if c["class"] == e["class"]), None)) and
                class_prereqs.get((enrolled_class["dcode"], enrolled_class["cno"]), set()).issubset(
                    student_passed_courses.get(s["ssn"], set())
                )
                for e in enrollment if e["ssn"] == s["ssn"]
            )
        ],
        key=lambda t: t["ssn"]
    )
    # All students  { ssn: ..., name: ..., major: ..., status: ...} who are enrolled in a class for which they have not satisfied all its prerequisites. 
    dataQuery_d = sorted(
        [
            s for s in student
            if any(
                (enrolled_class := next((c for c in class_ if c["class"] == e["class"]), None)) and
                not class_prereqs.get((enrolled_class["dcode"], enrolled_class["cno"]), set()).issubset(
                    student_passed_courses.get(s["ssn"], set())
                )
                for e in enrollment if e["ssn"] == s["ssn"]
            )
        ],
        key=lambda t: t["ssn"]
    )

    # Students named "John" who are enrolled in a class for which they haven't satisfied prerequisites
    dataQuery_e = sorted(
        [s for s in dataQuery_d if s["name"] == "John"],
        key=lambda t: t["ssn"]
    )  

    # Courses with no prerequisites
    dataQuery_f = sorted(
        [
            {"dcode": c["dcode"], "cno": c["cno"]}
            for c in course if not any(p["dcode"] == c["dcode"] and p["cno"] == c["cno"] for p in prereq)
        ],
        key=lambda t: (t["dcode"], t["cno"])
    )

    # Courses with prerequisites
    dataQuery_g = sorted(
        [
            {"dcode": c["dcode"], "cno": c["cno"]}
            for c in course if any(p["dcode"] == c["dcode"] and p["cno"] == c["cno"] for p in prereq)
        ],
        key=lambda t: (t["dcode"], t["cno"])
    )

    # Classes offered this semester that have prerequisites
    dataQuery_h = sorted(
        [
            c for c in class_
            if any(p["dcode"] == c["dcode"] and p["cno"] == c["cno"] for p in prereq)
        ],
        key=lambda t: t["class"]
    )

    # Students who received only A or B grades in all courses they have taken
    dataQuery_i = sorted(
        [
            s for s in student
            if all(t["grade"] in ["A", "B"] for t in transcript if t["ssn"] == s["ssn"])
        ],
        key=lambda t: t["ssn"]
    )

    # CS students currently enrolled in a class taught by professor Brodsky
    brodsky_id = next((f["ssn"] for f in faculty if f["name"] == "Brodsky"), None)
    dataQuery_j = sorted(
        [
            s for s in student
            if s["major"] == "CS" and any(
                c["instr"] == brodsky_id and c["class"] == e["class"]
                for c in class_ for e in enrollment if e["ssn"] == s["ssn"]
            )
        ],
        key=lambda t: t["ssn"]
    )

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
