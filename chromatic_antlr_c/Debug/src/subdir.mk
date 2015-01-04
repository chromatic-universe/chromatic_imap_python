################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/antlr_cppLexer.c \
../src/antlr_cppParser.c \
../src/chromatic_antlr_c.c 

OBJS += \
./src/antlr_cppLexer.o \
./src/antlr_cppParser.o \
./src/chromatic_antlr_c.o 

C_DEPS += \
./src/antlr_cppLexer.d \
./src/antlr_cppParser.d \
./src/chromatic_antlr_c.d 


# Each subdirectory must supply rules for building sources it contributes
src/%.o: ../src/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/develop/tools/antlr/libantlr3c-3.1.3/include -I/develop/tools/antlr/libantlr3c-3.1.3 -I/develop/workspace/chromatic_antlr_c/src -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@:%.o=%.d)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '

src/chromatic_antlr_c.o: ../src/chromatic_antlr_c.c
	@echo 'Building file: $<'
	@echo 'Invoking: GCC C Compiler'
	gcc -I/develop/tools/antlr/libantlr3c-3.1.3/include -I/develop/tools/antlr/libantlr3c-3.1.3 -O0 -g3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"src/chromatic_antlr_c.d" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


