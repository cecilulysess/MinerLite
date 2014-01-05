
#include <iostream>
#include <thread>
#include <chrono>
#include <cstdlib>
#include <string>
using std::cout;
using std::endl;


int main(int argc, char** argv){
	cout<<"MinerLite Started, wait for 2 seconds for running cgmienr.."<<endl;
	std::this_thread::sleep_for(std::chrono::milliseconds(2000));
	cout<<"Run cgminer"<<endl;

	std::string cmd("~/mining/cgminer/cgminer");
	if (argc < 2) {
		cout<<cmd<<endl;
	} else {
		cout<<"Run cgminer from: "<<argv[1]<<endl;
	}
	
	cout<<std::system(cmd.c_str())<<endl;
}