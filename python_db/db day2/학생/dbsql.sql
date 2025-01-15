create table if not exists etudents (
	id int auto_increment primary key,
    name varchar(100) not null,
    age int not null,
    grade varchar(100) not null,
    created_at timestamp default current_timestamp
);

create table if not exists enrollments (
	id int auto_increment primary key,
    student_id int not null,
    course_name varchar(100) not null,
    enrollments_date date not null,
    foreign key (student_id) references students(id) on delete cascade
);