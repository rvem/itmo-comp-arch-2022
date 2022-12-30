addi $s0, $0, 7
j jal_label # j 3
addi $s0, $0, 8
jal_label:
jal end_label # jal 5
addi $s0, $0, 9
end_label:
sw $ra, 0($0)