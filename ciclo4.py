< component
name = "ProjectDictionaryState" >
< dictionary
name = "Maycon" >
< words >
< w > insira < / w >
< / words >
< / dictionary >
< / component >


class CalculoImc {Maycon
/ **
* @ param args the command line arguments
* /
public static void main(String[ ] args) {

Float altura , peso , alturaemmetros , imc ;
String entradadedados , resposta ;


entradadedados = JOptionPane.showInputDialog("Digite o seu peso: ") ;
peso = Float.parseFloat(entradadedados) ;

entradadedados = JOptionPane.showInputDialog("Digite a sua altura em cm: ") ;
altura = Float.parseFloat(entradadedados) ;


alturaemmetros = altura / 100 ;

imc = peso / (alturaemmetros * alturaemmetros) ;
DecimalFormat df = new DecimalFormat("0.00") ;
resposta = df.format(imc) ;

if (imc < 16){
JOptionPane.showMessageDialog(null , "O imc é: " + resposta + ". Classificado em magreza leve") ;
} else if ((imc >= 16) & & (imc < 17)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em  magreza moderada") ;
} else if ((imc >= 17) & & (imc < 18.5)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em magreza leve ") ;
} else if ((imc >= 18.5) & & (imc < 25)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em Saudável") ;
} else if ((imc >= 25) & & (imc < 30)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em sobrepeso") ;
} else if ((imc >= 30) & & (imc < 35)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em obesidade Grau I ") ;
} else if ((imc >= 35) & & (imc < 40)){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em obesidade Grau II (severa) ") ;
} else if (imc > 40){
JOptionPane.showMessageDialog(null , "Seu IMC é: " + resposta + ". Classificado em obesidade Grau III (mórbida)") ;
}

}

}
