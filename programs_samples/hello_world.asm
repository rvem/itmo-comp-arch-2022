addi $t0, $0, 72 # H
beq $0, $0, mult2x8
fi:
addi $t0, $t0, 101 # e

addi $t1, $0, 8
loop1:
beq $t1, $0, fi1
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop1
fi1:

addi $t0, $t0, 108 # l

addi $t1, $0, 8
loop2:
beq $t1, $0, fi2
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop2
fi2:

addi $t0, $t0, 108 # l
sw $t0, 0($0)

addi $t0, $0, 111 # o

addi $t1, $0, 8
loop3:
beq $t1, $0, fi3
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop3
fi3:

addi $t0, $t0, 32 # space

addi $t1, $0, 8
loop4:
beq $t1, $0, fi4
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop4
fi4:

addi $t0, $t0, 119 # w

addi $t1, $0, 8
loop5:
beq $t1, $0, fi5
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop5
fi5:

addi $t0, $t0, 111 # o
sw $t0, 4($0)

addi $t0, $0, 114 # r

addi $t1, $0, 8
loop6:
beq $t1, $0, fi6
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop6
fi6:

addi $t0, $t0, 108 # l

addi $t1, $0, 8
loop7:
beq $t1, $0, fi7
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop7
fi7:

addi $t0, $t0, 100 # d

addi $t1, $0, 8
loop8:
beq $t1, $0, fi8
add $t0, $t0, $t0
sub $t1, $t1, $t2
beq $0, $0, loop8
fi8:

addi $t0, $t0, 33 # !
sw $t0, 8($0)



beq $0, $0, halt
mult2x8:
addi $t1, $0, 8
addi $t2, $0, 1

loop:
beq $t1, $0, fi

add $t0, $t0, $t0

sub $t1, $t1, $t2
beq $0, $0, loop
halt:
beq $0, $0, halt