# 组件A的Makefile（依赖component_b的动态库）
CC ?= gcc
CFLAGS ?= -Wall -Wextra -I$(INCLUDE_DEPENDENCIES) 
LDFLAGS ?= -L$(INCLUDE_DEPENDENCIES) -Wl,-rpath=$(INCLUDE_DEPENDENCIES)  # 指定动态库的搜索路径（组件B的目录）
LIBS ?= -lcomp2                  # 链接动态库（libb.so，省略前缀"lib"和后缀".so"）
TARGET ?= comp1              # 可执行文件目标

# 编译规则：依赖组件B的动态库
all: $(TARGET)

$(TARGET): comp1.c
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS) $(LIBS)

# 清理编译产物
clean:
	rm -f $(TARGET)
