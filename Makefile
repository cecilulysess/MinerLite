ifeq ("$(shell uname)", "Darwin")
	CCC = clang++
	CFLAGS = -g -std=c++11 -stdlib=libc++ -Wall
else
	CCC = g++
	CFLAGS = -std=c++0x -Wall -g
endif

OBJS = main.o 

run: $(OBJS)
	$(CCC) $(CFLAGS) -o run $(OBJS)

main.o: main.cpp
	$(CCC) $(CFLAGS) -c main.cpp


	
clean:
	rm -f run *.o
