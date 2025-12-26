; ModuleID = "relational_module"
target triple = "unknown-unknown-unknown"
target datalayout = ""

declare void @"_print_str"(i8* %".1")

declare void @"_print_int"(i32 %".1")

declare void @"_print_float"(double %".1")

declare i8* @"_create_table"(i8* %".1")

define i32 @"main"()
{
entry:
  %"x" = alloca i32
  store i32 10, i32* %"x"
  %"y" = alloca i32
  store i32 20, i32* %"y"
  %"x.1" = load i32, i32* %"x"
  %"y.1" = load i32, i32* %"y"
  %"addtmp" = add i32 %"x.1", %"y.1"
  %"res" = alloca i32
  store i32 %"addtmp", i32* %"res"
  %"res.1" = load i32, i32* %"res"
  call void @"_print_int"(i32 %"res.1")
  %".6" = bitcast [11 x i8]* @"str" to i8*
  %"msg" = alloca i8*
  store i8* %".6", i8** %"msg"
  %"msg.1" = load i8*, i8** %"msg"
  call void @"_print_str"(i8* %"msg.1")
  %".9" = bitcast [8 x i8]* @"str.1" to i8*
  %".10" = call i8* @"_create_table"(i8* %".9")
  %"db" = alloca i8*
  store i8* %".10", i8** %"db"
  ret i32 0
}

@"str" = internal constant [11 x i8] c"Hello LLVM\00"
@"str.1" = internal constant [8 x i8] c"MyTable\00"