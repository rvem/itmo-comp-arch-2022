## Материалы к лекции по языку Verilog

- [introduction.v](introduction.v): основной синтаксис, процедурное моделирование, конструкции времени
- [structural.v](structural.v): структурное моделирование. Определяем и тестируем модуль полусумматора

### Инструменты
- Icarus Verilog - симулятор, который мы используем. Для Windows: https://bleyer.org/icarus/. Для линукса ищите пакет в официальном репозитории своего дистрибутива. Для мака можно попробовать найти через Homebrew или MacPorts
- GTK Wave - визуализация сигналов из vcd файла: https://gtkwave.sourceforge.net/
- https://edaplayground.com - онлайн редактор для Верилога. В качестве симулятора можно выбрать Icarus Verilog

### Запуск симуляции с помощью симулятора Icarus Verilog
```
$ iverilog structural.v -s testbench
$ ./a.out
```

### Другие интересные материалы по Верилогу
- Подробный справочник: https://www.hdlworks.com/hdl_corner/verilog_ref/
- Последняя версия официальной спецификации: https://ieeexplore.ieee.org/document/1620780
- Подробное описание в английской Википедии: https://en.wikipedia.org/wiki/Verilog
- Статьи на английском по основам Верилога: https://www.chipverify.com/verilog/verilog-tutorial
