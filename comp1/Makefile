# comp1的Makefile（依赖comp2的动态库）
CC ?= gcc
CFLAGS ?= -Wall -Wextra -I$(DEP_LIB) -I$(DEP_INCLUDE)
LDFLAGS ?= -L$(DEP_LIB) -Wl,-rpath=/usr/lib  # 指定动态库的搜索路径（组件B的目录）
LIBS ?= -lcomp2                  # 链接动态库（libb.so，省略前缀"lib"和后缀".so"）
TARGET ?= $(OUTPUT_DIR)/comp1/usr/bin/comp1              # 可执行文件目标

# 编译规则：依赖组件B的动态库
all: $(TARGET)

$(TARGET): comp1.c
	mkdir -p $(OUTPUT_DIR)/comp1/usr/bin/
	$(CC) $(CFLAGS) -o $@ $< $(LDFLAGS) $(LIBS)

# 清理编译产物
clean:
	rm -f $(TARGET)
