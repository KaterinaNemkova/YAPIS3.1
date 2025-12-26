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
  %"val_1" = alloca double
  store double 0x4025000000000000, double* %"val_1"
  %"val_2" = alloca double
  store double 0x4012000000000000, double* %"val_2"
  %"val_1.1" = load double, double* %"val_1"
  %"val_2.1" = load double, double* %"val_2"
  %"fadd" = fadd double %"val_1.1", %"val_2.1"
  %"sum" = alloca double
  store double %"fadd", double* %"sum"
  %".5" = bitcast [13 x i8]* @"str" to i8*
  call void @"_print_str"(i8* %".5")
  %"sum.1" = load double, double* %"sum"
  call void @"_print_float"(double %"sum.1")
  %"val_1.2" = load double, double* %"val_1"
  %"val_2.2" = load double, double* %"val_2"
  %"fsub" = fsub double %"val_1.2", %"val_2.2"
  %"diff" = alloca double
  store double %"fsub", double* %"diff"
  %".9" = bitcast [13 x i8]* @"str.1" to i8*
  call void @"_print_str"(i8* %".9")
  %"diff.1" = load double, double* %"diff"
  call void @"_print_float"(double %"diff.1")
  %"val_1.3" = load double, double* %"val_1"
  %"val_2.3" = load double, double* %"val_2"
  %"fmul" = fmul double %"val_2.3", 0x4000000000000000
  %"fadd.1" = fadd double %"val_1.3", %"fmul"
  %"res" = alloca double
  store double %"fadd.1", double* %"res"
  %".13" = bitcast [17 x i8]* @"str.2" to i8*
  call void @"_print_str"(i8* %".13")
  %"res.1" = load double, double* %"res"
  call void @"_print_float"(double %"res.1")
  ret i32 0
}

@"str" = internal constant [13 x i8] c"Sum (15.00):\00"
@"str.1" = internal constant [13 x i8] c"Diff (6.00):\00"
@"str.2" = internal constant [17 x i8] c"Complex (19.50):\00"