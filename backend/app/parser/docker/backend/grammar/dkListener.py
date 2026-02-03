# Generated from ./backend/grammar/dk.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .dkParser import dkParser
else:
    from dkParser import dkParser

# This class defines a complete listener for a parse tree produced by dkParser.
class dkListener(ParseTreeListener):

    # Enter a parse tree produced by dkParser#dockerfile.
    def enterDockerfile(self, ctx:dkParser.DockerfileContext):
        pass

    # Exit a parse tree produced by dkParser#dockerfile.
    def exitDockerfile(self, ctx:dkParser.DockerfileContext):
        pass


    # Enter a parse tree produced by dkParser#instruction.
    def enterInstruction(self, ctx:dkParser.InstructionContext):
        pass

    # Exit a parse tree produced by dkParser#instruction.
    def exitInstruction(self, ctx:dkParser.InstructionContext):
        pass


    # Enter a parse tree produced by dkParser#from.
    def enterFrom(self, ctx:dkParser.FromContext):
        pass

    # Exit a parse tree produced by dkParser#from.
    def exitFrom(self, ctx:dkParser.FromContext):
        pass


    # Enter a parse tree produced by dkParser#run.
    def enterRun(self, ctx:dkParser.RunContext):
        pass

    # Exit a parse tree produced by dkParser#run.
    def exitRun(self, ctx:dkParser.RunContext):
        pass


    # Enter a parse tree produced by dkParser#cmd.
    def enterCmd(self, ctx:dkParser.CmdContext):
        pass

    # Exit a parse tree produced by dkParser#cmd.
    def exitCmd(self, ctx:dkParser.CmdContext):
        pass


    # Enter a parse tree produced by dkParser#label.
    def enterLabel(self, ctx:dkParser.LabelContext):
        pass

    # Exit a parse tree produced by dkParser#label.
    def exitLabel(self, ctx:dkParser.LabelContext):
        pass


    # Enter a parse tree produced by dkParser#maintainer.
    def enterMaintainer(self, ctx:dkParser.MaintainerContext):
        pass

    # Exit a parse tree produced by dkParser#maintainer.
    def exitMaintainer(self, ctx:dkParser.MaintainerContext):
        pass


    # Enter a parse tree produced by dkParser#expose.
    def enterExpose(self, ctx:dkParser.ExposeContext):
        pass

    # Exit a parse tree produced by dkParser#expose.
    def exitExpose(self, ctx:dkParser.ExposeContext):
        pass


    # Enter a parse tree produced by dkParser#env.
    def enterEnv(self, ctx:dkParser.EnvContext):
        pass

    # Exit a parse tree produced by dkParser#env.
    def exitEnv(self, ctx:dkParser.EnvContext):
        pass


    # Enter a parse tree produced by dkParser#add.
    def enterAdd(self, ctx:dkParser.AddContext):
        pass

    # Exit a parse tree produced by dkParser#add.
    def exitAdd(self, ctx:dkParser.AddContext):
        pass


    # Enter a parse tree produced by dkParser#copy.
    def enterCopy(self, ctx:dkParser.CopyContext):
        pass

    # Exit a parse tree produced by dkParser#copy.
    def exitCopy(self, ctx:dkParser.CopyContext):
        pass


    # Enter a parse tree produced by dkParser#entrypoint.
    def enterEntrypoint(self, ctx:dkParser.EntrypointContext):
        pass

    # Exit a parse tree produced by dkParser#entrypoint.
    def exitEntrypoint(self, ctx:dkParser.EntrypointContext):
        pass


    # Enter a parse tree produced by dkParser#volume.
    def enterVolume(self, ctx:dkParser.VolumeContext):
        pass

    # Exit a parse tree produced by dkParser#volume.
    def exitVolume(self, ctx:dkParser.VolumeContext):
        pass


    # Enter a parse tree produced by dkParser#user.
    def enterUser(self, ctx:dkParser.UserContext):
        pass

    # Exit a parse tree produced by dkParser#user.
    def exitUser(self, ctx:dkParser.UserContext):
        pass


    # Enter a parse tree produced by dkParser#workdir.
    def enterWorkdir(self, ctx:dkParser.WorkdirContext):
        pass

    # Exit a parse tree produced by dkParser#workdir.
    def exitWorkdir(self, ctx:dkParser.WorkdirContext):
        pass


    # Enter a parse tree produced by dkParser#arg.
    def enterArg(self, ctx:dkParser.ArgContext):
        pass

    # Exit a parse tree produced by dkParser#arg.
    def exitArg(self, ctx:dkParser.ArgContext):
        pass


    # Enter a parse tree produced by dkParser#onbuild.
    def enterOnbuild(self, ctx:dkParser.OnbuildContext):
        pass

    # Exit a parse tree produced by dkParser#onbuild.
    def exitOnbuild(self, ctx:dkParser.OnbuildContext):
        pass


    # Enter a parse tree produced by dkParser#stopsignal.
    def enterStopsignal(self, ctx:dkParser.StopsignalContext):
        pass

    # Exit a parse tree produced by dkParser#stopsignal.
    def exitStopsignal(self, ctx:dkParser.StopsignalContext):
        pass


    # Enter a parse tree produced by dkParser#healthcheck.
    def enterHealthcheck(self, ctx:dkParser.HealthcheckContext):
        pass

    # Exit a parse tree produced by dkParser#healthcheck.
    def exitHealthcheck(self, ctx:dkParser.HealthcheckContext):
        pass


    # Enter a parse tree produced by dkParser#shell.
    def enterShell(self, ctx:dkParser.ShellContext):
        pass

    # Exit a parse tree produced by dkParser#shell.
    def exitShell(self, ctx:dkParser.ShellContext):
        pass


    # Enter a parse tree produced by dkParser#platform_opt.
    def enterPlatform_opt(self, ctx:dkParser.Platform_optContext):
        pass

    # Exit a parse tree produced by dkParser#platform_opt.
    def exitPlatform_opt(self, ctx:dkParser.Platform_optContext):
        pass


    # Enter a parse tree produced by dkParser#as_opt.
    def enterAs_opt(self, ctx:dkParser.As_optContext):
        pass

    # Exit a parse tree produced by dkParser#as_opt.
    def exitAs_opt(self, ctx:dkParser.As_optContext):
        pass


    # Enter a parse tree produced by dkParser#name_opt.
    def enterName_opt(self, ctx:dkParser.Name_optContext):
        pass

    # Exit a parse tree produced by dkParser#name_opt.
    def exitName_opt(self, ctx:dkParser.Name_optContext):
        pass


    # Enter a parse tree produced by dkParser#param_opt.
    def enterParam_opt(self, ctx:dkParser.Param_optContext):
        pass

    # Exit a parse tree produced by dkParser#param_opt.
    def exitParam_opt(self, ctx:dkParser.Param_optContext):
        pass


    # Enter a parse tree produced by dkParser#image_spec.
    def enterImage_spec(self, ctx:dkParser.Image_specContext):
        pass

    # Exit a parse tree produced by dkParser#image_spec.
    def exitImage_spec(self, ctx:dkParser.Image_specContext):
        pass


    # Enter a parse tree produced by dkParser#label_pair.
    def enterLabel_pair(self, ctx:dkParser.Label_pairContext):
        pass

    # Exit a parse tree produced by dkParser#label_pair.
    def exitLabel_pair(self, ctx:dkParser.Label_pairContext):
        pass


    # Enter a parse tree produced by dkParser#env_pair.
    def enterEnv_pair(self, ctx:dkParser.Env_pairContext):
        pass

    # Exit a parse tree produced by dkParser#env_pair.
    def exitEnv_pair(self, ctx:dkParser.Env_pairContext):
        pass


    # Enter a parse tree produced by dkParser#env_single.
    def enterEnv_single(self, ctx:dkParser.Env_singleContext):
        pass

    # Exit a parse tree produced by dkParser#env_single.
    def exitEnv_single(self, ctx:dkParser.Env_singleContext):
        pass


    # Enter a parse tree produced by dkParser#path_spec.
    def enterPath_spec(self, ctx:dkParser.Path_specContext):
        pass

    # Exit a parse tree produced by dkParser#path_spec.
    def exitPath_spec(self, ctx:dkParser.Path_specContext):
        pass


    # Enter a parse tree produced by dkParser#shell_command_paths.
    def enterShell_command_paths(self, ctx:dkParser.Shell_command_pathsContext):
        pass

    # Exit a parse tree produced by dkParser#shell_command_paths.
    def exitShell_command_paths(self, ctx:dkParser.Shell_command_pathsContext):
        pass


    # Enter a parse tree produced by dkParser#json_command.
    def enterJson_command(self, ctx:dkParser.Json_commandContext):
        pass

    # Exit a parse tree produced by dkParser#json_command.
    def exitJson_command(self, ctx:dkParser.Json_commandContext):
        pass


    # Enter a parse tree produced by dkParser#json_array.
    def enterJson_array(self, ctx:dkParser.Json_arrayContext):
        pass

    # Exit a parse tree produced by dkParser#json_array.
    def exitJson_array(self, ctx:dkParser.Json_arrayContext):
        pass


    # Enter a parse tree produced by dkParser#shell_command.
    def enterShell_command(self, ctx:dkParser.Shell_commandContext):
        pass

    # Exit a parse tree produced by dkParser#shell_command.
    def exitShell_command(self, ctx:dkParser.Shell_commandContext):
        pass


    # Enter a parse tree produced by dkParser#health_none.
    def enterHealth_none(self, ctx:dkParser.Health_noneContext):
        pass

    # Exit a parse tree produced by dkParser#health_none.
    def exitHealth_none(self, ctx:dkParser.Health_noneContext):
        pass


    # Enter a parse tree produced by dkParser#health_cmd.
    def enterHealth_cmd(self, ctx:dkParser.Health_cmdContext):
        pass

    # Exit a parse tree produced by dkParser#health_cmd.
    def exitHealth_cmd(self, ctx:dkParser.Health_cmdContext):
        pass


    # Enter a parse tree produced by dkParser#options_opt.
    def enterOptions_opt(self, ctx:dkParser.Options_optContext):
        pass

    # Exit a parse tree produced by dkParser#options_opt.
    def exitOptions_opt(self, ctx:dkParser.Options_optContext):
        pass



del dkParser