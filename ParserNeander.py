#Parser neander
import sys

def opToBin(operacao):
	if operacao == "NOP":
		return "0000"
	if operacao == "STA":
		return "0001"
	if operacao == "LDA":
		return "0010"
	if operacao == "ADD":
		return "0011"
	if operacao == "OR":
		return "0100"
	if operacao == "AND":
		return "0101"
	if operacao == "NOT":
		return "0110"
	if operacao == "JMP":
		return "1000"
	if operacao == "JN":
		return "1001"
	if operacao == "JZ":
		return "1010"
	if operacao == "HLT":
		return "1111"
	if operacao == "SUB":
		return "1011"
	if operacao == "MULT":
		return "1100"
##livres 0111, 1011->SUB, 1100->MULT, 1101, 1110

'''
1100
1101
1110
0111
'''


#garantindo arquivo funcionando
arqLeitura = open (sys.argv[1],'a')
quebra="\n"
arqLeitura.writelines(quebra)
arqLeitura.close()
arqEscrita = open (sys.argv[2],'w')
nada=""
arqEscrita.writelines(nada)
arqEscrita.close()


#Parser
arqLeitura = open (sys.argv[1],'r')
arqEscrita = open (sys.argv[2],'a')
prog_Mneumo = arqLeitura.readlines()
textoTrad=[]
k=0
for linha in prog_Mneumo:
	if (len(linha)>1):
		i=0
		op=""
		str_num=""
		num=0
		binario=""
		while((linha[i]>='A' and linha[i]<='Z') or (linha[i]>='a' and linha[i]<='z')):
				op = op + linha[i]
				i=i+1
				print(op)
		op=op.upper()
		if ((op == "NOT") == (op=="NOP") == (op=="HLT")):
			i=i+1
			while(linha[i]>='0' and linha[i]<='9'):
				str_num = str_num + linha[i]
				i=i+1
				print(str_num)
				num=int(str_num,10)
				if num>255:
					num=(num%255)-1
				binario="{0:b}".format(num)
				while (len(binario)<8):
					binario="0"+binario


		oper=opToBin(op)
		
		#op = op+'\n'

		oper = oper+"0000"
		oper = oper+','
		#oper = oper+"  "+op
		arqEscrita.writelines(oper)
		#textoTrad.append(oper+"  "+op)

		if(len(binario)!=0):
			binario = binario+','
			arqEscrita.writelines(binario)
		#	textoTrad.append(binario)

#print(textoTrad)
arqLeitura.close()
arqEscrita.close()
