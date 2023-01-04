addi $s0, $0, 8
addi $s1, $0, 8
bne $s0, $s1, eq
add $t1, $s0, $s1
beq $0, $0, end
eq:
sub $t0, $s0, $s1
end: