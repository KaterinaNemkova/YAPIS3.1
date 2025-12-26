#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef enum {
    VAL_INT,
    VAL_FLOAT,
    VAL_STRING
} ValueType;

typedef struct {
    ValueType type;
    union {
        int i_val;
        double f_val;
        char* s_val;
    } data;
} Cell;

typedef struct {
    Cell* cells;
    int count;
    int capacity;
} Row;

typedef struct {
    char* name;
    char* type;
} Column;

typedef struct {
    char* name;

    Column* columns;
    int col_count;
    int col_capacity;

    Row* rows;
    int row_count;
    int row_capacity;
} Table;

Row temp_row = {0};


void init_row(Row* r) {
    r->count = 0;
    r->capacity = 10;
    r->cells = (Cell*)malloc(sizeof(Cell) * r->capacity);
}

void add_cell_to_row(Row* r, Cell c) {
    if (r->count >= r->capacity) {
        r->capacity *= 2;
        r->cells = (Cell*)realloc(r->cells, sizeof(Cell) * r->capacity);
    }
    r->cells[r->count++] = c;
}


void _print_str(char* str) { printf("%s\n", str); }
void _print_int(int val) { printf("%d\n", val); }
void _print_float(double val) { printf("%.2f\n", val); }

void* _create_table(char* name) {
    Table* t = (Table*)malloc(sizeof(Table));
    t->name = strdup(name);

    t->col_count = 0;
    t->col_capacity = 5;
    t->columns = (Column*)malloc(sizeof(Column) * t->col_capacity);

    t->row_count = 0;
    t->row_capacity = 10;
    t->rows = (Row*)malloc(sizeof(Row) * t->row_capacity);

    printf("[Runtime] Table '%s' created.\n", name);
    return (void*)t;
}

void _add_column(void* table_ptr, char* col_name, char* col_type) {
    Table* t = (Table*)table_ptr;
    if (t->col_count >= t->col_capacity) {
        t->col_capacity *= 2;
        t->columns = (Column*)realloc(t->columns, sizeof(Column) * t->col_capacity);
    }
    t->columns[t->col_count].name = strdup(col_name);
    t->columns[t->col_count].type = strdup(col_type);
    t->col_count++;
}


void _row_init() {
    if (temp_row.cells == NULL) {
        init_row(&temp_row);
    }
    for(int i=0; i<temp_row.count; i++) {
        if (temp_row.cells[i].type == VAL_STRING) {
        }
    }
    temp_row.count = 0;
}

void _row_add_int(int val) {
    Cell c; c.type = VAL_INT; c.data.i_val = val;
    add_cell_to_row(&temp_row, c);
}

void _row_add_float(double val) {
    Cell c; c.type = VAL_FLOAT; c.data.f_val = val;
    add_cell_to_row(&temp_row, c);
}

void _row_add_string(char* val) {
    Cell c; c.type = VAL_STRING; c.data.s_val = strdup(val);
    add_cell_to_row(&temp_row, c);
}

void _insert_row_commit(void* table_ptr) {
    Table* t = (Table*)table_ptr;

    if (t->row_count >= t->row_capacity) {
        t->row_capacity *= 2;
        t->rows = (Row*)realloc(t->rows, sizeof(Row) * t->row_capacity);
    }

    Row* new_row = &t->rows[t->row_count];
    init_row(new_row);

    for (int i = 0; i < temp_row.count; i++) {
        add_cell_to_row(new_row, temp_row.cells[i]);
    }

    t->row_count++;
}

void _print_table_full(void* table_ptr) {
    Table* t = (Table*)table_ptr;
    printf("\n--- Table: %s ---\n", t->name);

    for (int i = 0; i < t->col_count; i++) {
        printf("%s\t", t->columns[i].name);
    }
    printf("\n");

    for (int i = 0; i < t->row_count; i++) {
        Row* r = &t->rows[i];
        for (int j = 0; j < r->count; j++) {
            Cell* c = &r->cells[j];
            if (c->type == VAL_INT) printf("%d\t", c->data.i_val);
            else if (c->type == VAL_FLOAT) printf("%.2f\t", c->data.f_val);
            else if (c->type == VAL_STRING) printf("%s\t", c->data.s_val);
        }
        printf("\n");
    }
}