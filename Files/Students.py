
class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass

try: 
    file_name = input ("\n\tFile name: ")
    with open(file_name, "rt") as file:
        content = file.readlines()
        if len(content) == 0:
            raise FileEmpty("The file is empty")
        
        student_dict={}
        for line in content:
            data = line.split()
            if len(data) != 3:
                raise BadLine("The file contents is not correct")
            
            first_name, last_name, note_str = data
            note = float(note_str)
            name_student = first_name + " " + last_name
            
            if name_student in student_dict:
                student_dict[name_student] += note
            else:
                student_dict[name_student] = note
                
    sorted_student_dict = sorted(student_dict.items(), key=lambda x: x[0])
        
    max_name_length = max(len(name) for name, _ in sorted_student_dict)
    max_note_length = max(len(str(note)) for _, note in sorted_student_dict)
        
    for key, value in sorted_student_dict:
        print(f"{key:<{max_name_length}} {value:<{max_note_length}.2f}")
        
except StudentsDataException as e:
    print ("Exception: ", e)
finally:
    if 'file' in locals() and not file.closed:
        file.close()
   
    