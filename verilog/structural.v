// Реализация логического вентиля NOT с помощью структурных примитивов
module not_gate(in, out);
  // Входные порты помечаются как input, выходные как output
  input wire in;
  output wire out;
  // Ключевое слово wire для обозначения типа данных можно опустить,
  // тогда оно подставится неявно, например:
  /*
    input in;
    output out;
  */

  supply1 vdd; // Напряжение питания
  supply0 gnd; // Напряжение земли

  // p-канальный транзистор, сток = out, исток = vdd, затвор = in
  pmos pmos1(out, vdd, in); // (сток, исток, база)
  // n-канальный транзистор, сток = out, исток = gnd, затвор = in
  nmos nmos1(out, gnd, in);
endmodule

// Реализация NAND с помощью структурных примитивов
module nand_gate(in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;

  supply0 gnd;
  supply1 pwr;

  // С помощью типа wire можно определять промежуточные провода для соединения элементов.
  // В данном случае nmos1_out соединяет сток транзистора nmos1 и исток транзистора nmos2.
  wire nmos1_out;

  // 2 p-канальных и 2 n-канальных транзистора
  pmos pmos1(out, pwr, in1);
  pmos pmos2(out, pwr, in2);
  nmos nmos1(nmos1_out, gnd, in1);
  nmos nmos2(out, nmos1_out, in2);
endmodule

// Реализация NOR с помощью структурных примитивов
module nor_gate(in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;

  supply0 gnd;
  supply1 pwr;

  // Промежуточный провод, чтобы содединить сток pmos1 и исток pmos2
  wire pmos1_out;

  pmos pmos1(pmos1_out, pwr, in1);
  pmos pmos2(out, pmos1_out, in2);
  nmos nmos1(out, gnd, in1);
  nmos nmos2(out, gnd, in2);
endmodule

// Реализация AND с помощью NAND и NOT
module and_gate(in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;

  // Промежуточный провод, чтобы передать выход вентиля NAND на вход вентилю NOT
  wire nand_out;

  // Схема для формулы AND(in1, in2) = NOT(NAND(in1, in2))
  nand_gate nand_gate1(in1, in2, nand_out);
  not_gate not_gate1(nand_out, out);
endmodule

// Реализация OR с помощью NOR и NOT
module or_gate(in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;

  wire nor_out;

  // Схема для формулы OR(in1, in2) = NOT(NOR(in1, in2))
  nor_gate nor_gate1(in1, in2, nor_out);
  not_gate not_gate1(nor_out, out);
endmodule

// Реализация XOR с помощью NOT, AND, OR
module xor_gate(in1, in2, out);
  input wire in1;
  input wire in2;
  output wire out;

  wire not_in1;
  wire not_in2;

  wire and_out1;
  wire and_out2;

  wire or_out1;

  // Формула: XOR(in1, in2) = OR(AND(in1, NOT(in2)), AND(NOT(in1), in2))

  not_gate not_gate1(in1, not_in1);
  not_gate not_gate2(in2, not_in2);

  and_gate and_gate1(in1, not_in2, and_out1);
  and_gate and_gate2(not_in1, in2, and_out2);

  or_gate or_gate1(and_out1, and_out2, out);
endmodule

// Полусумматор
module half_adder(a, b, c_out, s);
  input wire a;
  input wire b;
  output wire c_out;
  output wire s;

  /*
    Таблица истинности для полусумматора
    a b | c_out | s
    0 0 | 0     | 0
    0 1 | 0     | 1
    1 0 | 0     | 1
    1 1 | 1     | 0
  */

  // c_out вычисляется как AND от a и b
  and_gate and_gate1(a, b, c_out);

  // s вычисляется как XOR от a и b
  xor_gate xor_gate1(a, b, s);
endmodule

// testbench -- модуль для процедурного тестирования нашей схемы
module testbench();
  reg a, b;
  wire c_out;
  wire s;
  half_adder ha1(a, b, c_out, s);

  // Сохранять сигналы в файл
  initial begin
    $dumpfile("./dump.vcd");
    $dumpvars;
  end

  initial begin
    // Переберем все возможные значения входных параметров

    a = 0;
    b = 0;
    // Делаем паузу в одну временную единицу, чтобы быть гарантировать, что
    // выходы модуля half_adder обновились до нового значения
    #1;
    // Вывести выходные параметры модуля half_adder
    $display("a = %b, b = %b => c_out = %b, s = %b", a, b, c_out, s);

    a = 0;
    b = 1;
    #1;
    $display("a = %b, b = %b => c_out = %b, s = %b", a, b, c_out, s);

    a = 1;
    b = 0;
    #1;
    $display("a = %b, b = %b => c_out = %b, s = %b", a, b, c_out, s);

    a = 1;
    b = 1;
    #1;
    $display("a = %b, b = %b => c_out = %b, s = %b", a, b, c_out, s);

  end
endmodule
