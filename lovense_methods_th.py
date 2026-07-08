# -*- coding: utf-8 -*-
LOVENSE_METHODS_TH = {
        "heading": "ตั้งค่า Lovense บน SplitCam — 3 ขั้นตอน",
        "lead": "ทำตามการตั้งค่า 3 ขั้นตอนของ Lovense เอง <strong>Cam Extension</strong> จะอ่าน"
                "ทิปจากเว็บแคมของคุณ, <strong>Lovense Connect</strong> คือตัวเชื่อม Bluetooth ไปยัง"
                "ของเล่นของคุณ และ <strong>SplitCam Toolset</strong> จะวางโอเวอร์เลย์ Lovense ไว้ใน"
                "SplitCam ซึ่งถ่ายทอดสดผ่าน RTMP ทุกอย่างฟรี ปุ่มดาวน์โหลดจะเลือกให้ตรงกับ"
                "ระบบของคุณโดยอัตโนมัติ",
        "stage_word": "ขั้นตอน",
        "get_label": "ดาวน์โหลด",
        "do_label": "จากนั้น",
        "stages": [
            {
                "title": "Lovense Cam Extension",
                "role": "อ่านทิปจากเว็บแคมของคุณ — ติดตั้งลงใน Chrome หรือ Edge",
                "get": ["camext"],
                "steps": [
                    "ดาวน์โหลด Cam Extension แล้วแตกไฟล์ zip",
                    "เปิด <strong>chrome://extensions</strong> (หรือ <strong>edge://extensions</strong>) "
                    "เปิด <strong>Developer mode</strong> ที่มุมขวาบน คลิก <strong>Load unpacked</strong> "
                    "แล้วเลือกโฟลเดอร์ <em>lovense_cam</em> ที่แตกไฟล์ไว้",
                    "คลิกไอคอน Lovense บนแถบเครื่องมือ แล้วเข้าสู่ระบบด้วยบัญชี Lovense ของคุณ",
                ],
            },
            {
                "title": "Lovense Connect",
                "role": "ตัวเชื่อมที่สื่อสารกับของเล่นของคุณผ่าน Bluetooth",
                "get": ["connect"],
                "steps": [
                    "บนคอมพิวเตอร์: ติดตั้ง Lovense Connect (แนะนำให้ใช้อะแดปเตอร์ Bluetooth USB ของ Lovense) "
                    "บนโทรศัพท์: ดาวน์โหลดแอป Lovense Connect จาก Google Play หรือ App Store",
                    "เปิดของเล่นของคุณแล้วจับคู่ใน Connect จนกว่าจะขึ้นว่าเชื่อมต่อแล้ว บนแอปโทรศัพท์ "
                    "ให้สแกน QR code ที่แสดงบนคอมพิวเตอร์ของคุณเพื่อเชื่อมทั้งสองเข้าด้วยกัน",
                ],
            },
            {
                "title": "SplitCam + Toolset",
                "role": "แสดงโอเวอร์เลย์ Lovense ใน SplitCam และถ่ายทอดสตรีมของคุณ",
                "get": ["splitcam", "toolset"],
                "steps": [
                    "ติดตั้ง SplitCam แล้วติดตั้ง Lovense SplitCam Toolset — ปลั๊กอินที่เพิ่ม"
                    "โอเวอร์เลย์ Lovense เข้าไปใน SplitCam",
                    "ใน Cam Extension คลิก <strong>+</strong> เพื่อเพิ่มเว็บแคมของคุณ (Chaturbate, "
                    "Stripchat, …) แล้วตั้งค่าเมนูทิปของคุณ จากนั้นเปิดแท็บ <strong>Video Feedback</strong> "
                    "แล้วเลือก <strong>SplitCam</strong> จากรายการ (OBS / SplitCam / Streamster)",
                    "ใน SplitCam ให้เพิ่มแหล่ง <strong>Lovense</strong> ที่ Toolset ลงทะเบียนไว้ — "
                    "โอเวอร์เลย์เมนูทิป / สถานะของเล่นจะปรากฏบนฉากของคุณ ให้วางไว้เหนือเลเยอร์อื่น ๆ",
                    "เพิ่มกล้องของคุณ วาง RTMP key ของเว็บแคมของคุณใน <strong>Stream "
                    "Settings</strong> ของ SplitCam แล้วคลิก <strong>Go Live</strong> — โอเวอร์เลย์และของเล่นจะตอบสนองต่อทิป",
                ],
            },
        ],
}
