def create_student_table():
    """
    학생 정보 테이블 생성쿼리
    """
    return """
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT NOT NULL,
        grade VARCHAR(100) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
def create_enrollments_table():
    """
    학생 수강 정보 테이블 생성 쿼리
    """
    return """
    CREATE TABLE IF NOT EXISTS enrollments (
        id INT AUTO_INCREMENT PRIMARY KEY,
        student_id INT NOT NULL,
        course_name VARCHAR(100) NOT NULL,
        enrollments_date DATE NOT NULL,
        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE
    );
    """
    
def insert_student():
    """
    학생 정보 삽입 쿼리(이름, 나이, 학년, 날짜) 날짜는 기본값으로 들어감.
    """
    return """INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)"""

def insert_enrollment():
    """
    학생 수강 정보 삽입 쿼리
    """
    return """insert into enrollments (student_id, course_name, enrollments_date) values (%s, %s, %s)"""

def select_student_with_enrollments():
    """
    학생 정보와 수강 정보를 조인하여 조회하는 쿼리
    """
    return """
        SELECT s.id as student_id,
            s.name as student_name,
            s.age as student_age,
            s.grade as student_grade,
            e.course_name as course_name,
            e.enrollments_date as enrollments_date
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
    """
def select_student_with_enrollments_one():
    """
    특정 학생 정보와 수강 정보를 조인하여 조회하는 쿼리
    """
    return """
        SELECT s.id as student_id,
            s.name as student_name,
            s.age as student_age,
            s.grade as student_grade,
            e.course_name as course_name,
            e.enrollments_date as enrollments_date
        FROM students s
        LEFT JOIN enrollments e ON s.id = e.student_id
        WHERE s.name=%s
    """
def update_student():
    """
    학생 정보 수정
    """
    return """
        UPDATE students SET age = %s, grade = %s WHERE id = %s"""

def select_students_one():
    return """select * from students where id=%s"""