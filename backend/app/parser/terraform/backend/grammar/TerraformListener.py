# Generated from ./backend/grammar/Terraform.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TerraformParser import TerraformParser
else:
    from TerraformParser import TerraformParser

# This class defines a complete listener for a parse tree produced by TerraformParser.
class TerraformListener(ParseTreeListener):

    # Enter a parse tree produced by TerraformParser#file.
    def enterFile(self, ctx:TerraformParser.FileContext):
        pass

    # Exit a parse tree produced by TerraformParser#file.
    def exitFile(self, ctx:TerraformParser.FileContext):
        pass


    # Enter a parse tree produced by TerraformParser#statement.
    def enterStatement(self, ctx:TerraformParser.StatementContext):
        pass

    # Exit a parse tree produced by TerraformParser#statement.
    def exitStatement(self, ctx:TerraformParser.StatementContext):
        pass


    # Enter a parse tree produced by TerraformParser#block.
    def enterBlock(self, ctx:TerraformParser.BlockContext):
        pass

    # Exit a parse tree produced by TerraformParser#block.
    def exitBlock(self, ctx:TerraformParser.BlockContext):
        pass


    # Enter a parse tree produced by TerraformParser#body.
    def enterBody(self, ctx:TerraformParser.BodyContext):
        pass

    # Exit a parse tree produced by TerraformParser#body.
    def exitBody(self, ctx:TerraformParser.BodyContext):
        pass


    # Enter a parse tree produced by TerraformParser#list.
    def enterList(self, ctx:TerraformParser.ListContext):
        pass

    # Exit a parse tree produced by TerraformParser#list.
    def exitList(self, ctx:TerraformParser.ListContext):
        pass


    # Enter a parse tree produced by TerraformParser#value.
    def enterValue(self, ctx:TerraformParser.ValueContext):
        pass

    # Exit a parse tree produced by TerraformParser#value.
    def exitValue(self, ctx:TerraformParser.ValueContext):
        pass



del TerraformParser