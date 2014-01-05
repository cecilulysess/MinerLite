#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
using std::cout;
using std::endl;


int main(){
	cout<<"Start"<<endl;
	std::this_thread::sleep_for(std::chrono::milliseconds(2000));
	cout<<"2 secs later"<<endl;
	cout<<std::system("ls -l")<<endl;
}