#include <iostream>
#include <thread>
#include <vector>
#include <iomanip>
#include <mutex>

using namespace std;

// Định nghĩa hằng số
const int PAGE_SIZE = 1 << 20;  // 2^20 = 1048576 phần tử
const int NUM_THREADS = 1 << 10; // 2^10 = 1024 threads
const int ELEMENTS_PER_THREAD = PAGE_SIZE / NUM_THREADS; // 1024 phần tử/thread

// Biến toàn cục
vector<double> PT(PAGE_SIZE);
vector<double> ThreadSum(NUM_THREADS);
double Sum = 0;
mutex mtx;

// Hàm xử lý cho mỗi thread
void processThread(int threadId) {
    int start = threadId * ELEMENTS_PER_THREAD;
    int end = start + ELEMENTS_PER_THREAD;
    double localSum = 0;

    // Khởi tạo giá trị và tính tổng cho thread
    for (int i = start; i < end; i++) {
        PT[i] = i * 1.0;
        localSum += PT[i];
    }

    // Lưu tổng của thread
    ThreadSum[threadId] = localSum;

    // In thông tin thread (thread-safe)
    lock_guard<mutex> lock(mtx);
    cout << "Thread " << threadId << " xu ly tu " << start 
         << " den " << end - 1 << endl;
    cout << "ThreadSum[" << threadId << "] = " << fixed 
         << setprecision(1) << localSum << endl;
}

int main() {
    // In thông tin sinh viên
    cout << "* Bai thi ket thuc mon: Lap trinh tren Linux.\n";
    cout << "* Ho va ten: NGUYEN VAN A\n";
    cout << "* Nhom: Nh19??\n";
    cout << "* Masv: ??????????\n";
    cout << "* De so: 05.\n";
    cout << "*\n";

    // Tạo và chạy các threads
    vector<thread> threads;
    for (int i = 0; i < NUM_THREADS; i++) {
        threads.push_back(thread(processThread, i));
    }

    // Đợi tất cả threads hoàn thành
    for (auto& th : threads) {
        th.join();
    }

    // Tính tổng cuối cùng
    for (double threadSum : ThreadSum) {
        Sum += threadSum;
    }

    // In kết quả cuối cùng
    cout << "\nTong cua tat ca cac thread: " << fixed 
         << setprecision(1) << Sum << endl;

    return 0;
}
