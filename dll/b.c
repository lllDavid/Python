#include <windows.h>

__declspec(dllexport) void show_message() {
    MessageBoxW(NULL, L"<Injected Message>", L"Message", MB_OK);
}

BOOL APIENTRY DllMain(HMODULE hModule, DWORD  ul_reason_for_call, LPVOID lpReserved) {
    if (ul_reason_for_call == DLL_PROCESS_ATTACH) {
        show_message();
    }
    return TRUE;
}
