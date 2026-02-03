# Generated from ./backend/grammar/nginx.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .nginxParser import nginxParser
else:
    from nginxParser import nginxParser

# This class defines a complete listener for a parse tree produced by nginxParser.
class nginxListener(ParseTreeListener):

    # Enter a parse tree produced by nginxParser#config.
    def enterConfig(self, ctx:nginxParser.ConfigContext):
        pass

    # Exit a parse tree produced by nginxParser#config.
    def exitConfig(self, ctx:nginxParser.ConfigContext):
        pass


    # Enter a parse tree produced by nginxParser#directive.
    def enterDirective(self, ctx:nginxParser.DirectiveContext):
        pass

    # Exit a parse tree produced by nginxParser#directive.
    def exitDirective(self, ctx:nginxParser.DirectiveContext):
        pass


    # Enter a parse tree produced by nginxParser#http.
    def enterHttp(self, ctx:nginxParser.HttpContext):
        pass

    # Exit a parse tree produced by nginxParser#http.
    def exitHttp(self, ctx:nginxParser.HttpContext):
        pass


    # Enter a parse tree produced by nginxParser#server.
    def enterServer(self, ctx:nginxParser.ServerContext):
        pass

    # Exit a parse tree produced by nginxParser#server.
    def exitServer(self, ctx:nginxParser.ServerContext):
        pass


    # Enter a parse tree produced by nginxParser#upstream.
    def enterUpstream(self, ctx:nginxParser.UpstreamContext):
        pass

    # Exit a parse tree produced by nginxParser#upstream.
    def exitUpstream(self, ctx:nginxParser.UpstreamContext):
        pass


    # Enter a parse tree produced by nginxParser#location.
    def enterLocation(self, ctx:nginxParser.LocationContext):
        pass

    # Exit a parse tree produced by nginxParser#location.
    def exitLocation(self, ctx:nginxParser.LocationContext):
        pass


    # Enter a parse tree produced by nginxParser#limit_except.
    def enterLimit_except(self, ctx:nginxParser.Limit_exceptContext):
        pass

    # Exit a parse tree produced by nginxParser#limit_except.
    def exitLimit_except(self, ctx:nginxParser.Limit_exceptContext):
        pass


    # Enter a parse tree produced by nginxParser#if_stmt.
    def enterIf_stmt(self, ctx:nginxParser.If_stmtContext):
        pass

    # Exit a parse tree produced by nginxParser#if_stmt.
    def exitIf_stmt(self, ctx:nginxParser.If_stmtContext):
        pass


    # Enter a parse tree produced by nginxParser#include.
    def enterInclude(self, ctx:nginxParser.IncludeContext):
        pass

    # Exit a parse tree produced by nginxParser#include.
    def exitInclude(self, ctx:nginxParser.IncludeContext):
        pass


    # Enter a parse tree produced by nginxParser#lua_code.
    def enterLua_code(self, ctx:nginxParser.Lua_codeContext):
        pass

    # Exit a parse tree produced by nginxParser#lua_code.
    def exitLua_code(self, ctx:nginxParser.Lua_codeContext):
        pass


    # Enter a parse tree produced by nginxParser#parameter.
    def enterParameter(self, ctx:nginxParser.ParameterContext):
        pass

    # Exit a parse tree produced by nginxParser#parameter.
    def exitParameter(self, ctx:nginxParser.ParameterContext):
        pass


    # Enter a parse tree produced by nginxParser#http_method.
    def enterHttp_method(self, ctx:nginxParser.Http_methodContext):
        pass

    # Exit a parse tree produced by nginxParser#http_method.
    def exitHttp_method(self, ctx:nginxParser.Http_methodContext):
        pass


    # Enter a parse tree produced by nginxParser#if_cond.
    def enterIf_cond(self, ctx:nginxParser.If_condContext):
        pass

    # Exit a parse tree produced by nginxParser#if_cond.
    def exitIf_cond(self, ctx:nginxParser.If_condContext):
        pass


    # Enter a parse tree produced by nginxParser#if_body.
    def enterIf_body(self, ctx:nginxParser.If_bodyContext):
        pass

    # Exit a parse tree produced by nginxParser#if_body.
    def exitIf_body(self, ctx:nginxParser.If_bodyContext):
        pass


    # Enter a parse tree produced by nginxParser#if_param.
    def enterIf_param(self, ctx:nginxParser.If_paramContext):
        pass

    # Exit a parse tree produced by nginxParser#if_param.
    def exitIf_param(self, ctx:nginxParser.If_paramContext):
        pass


    # Enter a parse tree produced by nginxParser#if_compare.
    def enterIf_compare(self, ctx:nginxParser.If_compareContext):
        pass

    # Exit a parse tree produced by nginxParser#if_compare.
    def exitIf_compare(self, ctx:nginxParser.If_compareContext):
        pass


    # Enter a parse tree produced by nginxParser#if_regexp.
    def enterIf_regexp(self, ctx:nginxParser.If_regexpContext):
        pass

    # Exit a parse tree produced by nginxParser#if_regexp.
    def exitIf_regexp(self, ctx:nginxParser.If_regexpContext):
        pass


    # Enter a parse tree produced by nginxParser#if_function.
    def enterIf_function(self, ctx:nginxParser.If_functionContext):
        pass

    # Exit a parse tree produced by nginxParser#if_function.
    def exitIf_function(self, ctx:nginxParser.If_functionContext):
        pass


    # Enter a parse tree produced by nginxParser#if_str.
    def enterIf_str(self, ctx:nginxParser.If_strContext):
        pass

    # Exit a parse tree produced by nginxParser#if_str.
    def exitIf_str(self, ctx:nginxParser.If_strContext):
        pass


    # Enter a parse tree produced by nginxParser#upstream_servers.
    def enterUpstream_servers(self, ctx:nginxParser.Upstream_serversContext):
        pass

    # Exit a parse tree produced by nginxParser#upstream_servers.
    def exitUpstream_servers(self, ctx:nginxParser.Upstream_serversContext):
        pass


    # Enter a parse tree produced by nginxParser#location_match.
    def enterLocation_match(self, ctx:nginxParser.Location_matchContext):
        pass

    # Exit a parse tree produced by nginxParser#location_match.
    def exitLocation_match(self, ctx:nginxParser.Location_matchContext):
        pass


    # Enter a parse tree produced by nginxParser#name.
    def enterName(self, ctx:nginxParser.NameContext):
        pass

    # Exit a parse tree produced by nginxParser#name.
    def exitName(self, ctx:nginxParser.NameContext):
        pass


    # Enter a parse tree produced by nginxParser#value.
    def enterValue(self, ctx:nginxParser.ValueContext):
        pass

    # Exit a parse tree produced by nginxParser#value.
    def exitValue(self, ctx:nginxParser.ValueContext):
        pass


    # Enter a parse tree produced by nginxParser#on.
    def enterOn(self, ctx:nginxParser.OnContext):
        pass

    # Exit a parse tree produced by nginxParser#on.
    def exitOn(self, ctx:nginxParser.OnContext):
        pass


    # Enter a parse tree produced by nginxParser#off.
    def enterOff(self, ctx:nginxParser.OffContext):
        pass

    # Exit a parse tree produced by nginxParser#off.
    def exitOff(self, ctx:nginxParser.OffContext):
        pass


    # Enter a parse tree produced by nginxParser#path.
    def enterPath(self, ctx:nginxParser.PathContext):
        pass

    # Exit a parse tree produced by nginxParser#path.
    def exitPath(self, ctx:nginxParser.PathContext):
        pass


    # Enter a parse tree produced by nginxParser#path_component.
    def enterPath_component(self, ctx:nginxParser.Path_componentContext):
        pass

    # Exit a parse tree produced by nginxParser#path_component.
    def exitPath_component(self, ctx:nginxParser.Path_componentContext):
        pass


    # Enter a parse tree produced by nginxParser#http_name.
    def enterHttp_name(self, ctx:nginxParser.Http_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#http_name.
    def exitHttp_name(self, ctx:nginxParser.Http_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#server_name.
    def enterServer_name(self, ctx:nginxParser.Server_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#server_name.
    def exitServer_name(self, ctx:nginxParser.Server_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#upstream_name.
    def enterUpstream_name(self, ctx:nginxParser.Upstream_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#upstream_name.
    def exitUpstream_name(self, ctx:nginxParser.Upstream_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#location_name.
    def enterLocation_name(self, ctx:nginxParser.Location_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#location_name.
    def exitLocation_name(self, ctx:nginxParser.Location_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#if_name.
    def enterIf_name(self, ctx:nginxParser.If_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#if_name.
    def exitIf_name(self, ctx:nginxParser.If_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#include_name.
    def enterInclude_name(self, ctx:nginxParser.Include_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#include_name.
    def exitInclude_name(self, ctx:nginxParser.Include_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#limit_except_name.
    def enterLimit_except_name(self, ctx:nginxParser.Limit_except_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#limit_except_name.
    def exitLimit_except_name(self, ctx:nginxParser.Limit_except_nameContext):
        pass


    # Enter a parse tree produced by nginxParser#lua_code_name.
    def enterLua_code_name(self, ctx:nginxParser.Lua_code_nameContext):
        pass

    # Exit a parse tree produced by nginxParser#lua_code_name.
    def exitLua_code_name(self, ctx:nginxParser.Lua_code_nameContext):
        pass



del nginxParser