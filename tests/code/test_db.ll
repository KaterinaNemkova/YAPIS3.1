; ModuleID = "relational_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"_print_str"(i8* %".1")

declare void @"_print_int"(i32 %".1")

declare void @"_print_float"(double %".1")

declare i8* @"_create_table"(i8* %".1")

declare void @"_add_column"(i8* %".1", i8* %".2", i8* %".3")

declare void @"_row_init"()

declare void @"_row_add_int"(i32 %".1")

declare void @"_row_add_float"(double %".1")

declare void @"_row_add_string"(i8* %".1")

declare void @"_insert_row_commit"(i8* %".1")

declare void @"_print_table_full"(i8* %".1")

define i32 @"main"()
{
entry:
  %".2" = bitcast [10 x i8]* @"str" to i8*
  %".3" = call i8* @"_create_table"(i8* %".2")
  %"db" = alloca i8*
  store i8* %".3", i8** %"db"
  %"db.1" = load i8*, i8** %"db"
  %".5" = bitcast [3 x i8]* @"str.1" to i8*
  %".6" = bitcast [4 x i8]* @"str.2" to i8*
  call void @"_add_column"(i8* %"db.1", i8* %".5", i8* %".6")
  %"db.2" = load i8*, i8** %"db"
  %".8" = bitcast [5 x i8]* @"str.3" to i8*
  %".9" = bitcast [7 x i8]* @"str.4" to i8*
  call void @"_add_column"(i8* %"db.2", i8* %".8", i8* %".9")
  %"db.3" = load i8*, i8** %"db"
  %".11" = bitcast [7 x i8]* @"str.5" to i8*
  %".12" = bitcast [6 x i8]* @"str.6" to i8*
  call void @"_add_column"(i8* %"db.3", i8* %".11", i8* %".12")
  %"db.4" = load i8*, i8** %"db"
  call void @"_row_init"()
  call void @"_row_add_int"(i32 1)
  %".16" = bitcast [5 x i8]* @"str.7" to i8*
  call void @"_row_add_string"(i8* %".16")
  call void @"_row_add_float"(double 0x40e86a1000000000)
  call void @"_insert_row_commit"(i8* %"db.4")
  %"db.5" = load i8*, i8** %"db"
  call void @"_row_init"()
  call void @"_row_add_int"(i32 2)
  %".22" = bitcast [5 x i8]* @"str.8" to i8*
  call void @"_row_add_string"(i8* %".22")
  call void @"_row_add_float"(double 0x40e5f90000000000)
  call void @"_insert_row_commit"(i8* %"db.5")
  %"db.6" = load i8*, i8** %"db"
  call void @"_row_init"()
  call void @"_row_add_int"(i32 3)
  %".28" = bitcast [6 x i8]* @"str.9" to i8*
  call void @"_row_add_string"(i8* %".28")
  call void @"_row_add_float"(double 0x40ed4c0000000000)
  call void @"_insert_row_commit"(i8* %"db.6")
  %".32" = bitcast [31 x i8]* @"str.10" to i8*
  call void @"_print_str"(i8* %".32")
  %"db.7" = load i8*, i8** %"db"
  call void @"_print_table_full"(i8* %"db.7")
  ret i32 0
}

@"str" = internal constant [10 x i8] c"Employees\00"
@"str.1" = internal constant [3 x i8] c"ID\00"
@"str.2" = internal constant [4 x i8] c"int\00"
@"str.3" = internal constant [5 x i8] c"Name\00"
@"str.4" = internal constant [7 x i8] c"string\00"
@"str.5" = internal constant [7 x i8] c"Salary\00"
@"str.6" = internal constant [6 x i8] c"float\00"
@"str.7" = internal constant [5 x i8] c"Ivan\00"
@"str.8" = internal constant [5 x i8] c"Petr\00"
@"str.9" = internal constant [6 x i8] c"Maria\00"
@"str.10" = internal constant [31 x i8] c"Database created successfully.\00"