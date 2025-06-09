# import streamlit as st
# import base64
# import json
# import subprocess

# # Input for server address with default localhost
# server_url = st.sidebar.text_input(
#     "Server URL", "http://localhost:8000/",
#     help="Nhập địa chỉ server (ví dụ: http://localhost:8000/)"
# )


# def save_json(data, filename="g.json"):  
#     with open(filename, "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=4)


# def send_curl(json_file="g.json"):
#     if not server_url.endswith("/"):
#         url = server_url + "/"
#     else:
#         url = server_url

#     st.info(f"Đang gửi yêu cầu curl tới {url}")
#     try:
#         result = subprocess.run(
#             [
#                 "curl", "-s", "-X", "POST",
#                 "-F", f"file=@{json_file}",
#                 url
#             ],
#             capture_output=True,
#             text=True
#         )
#         st.info("📤 Đã gửi yêu cầu curl tới server.")
#         # Hiển thị phản hồi
#         try:
#             parsed = json.loads(result.stdout)
#             formatted = json.dumps(parsed, ensure_ascii=False, indent=2)
#             st.code(formatted, language="json")
#         except json.JSONDecodeError:
#             st.code(result.stdout or "Không có phản hồi", language="bash")

#         if result.stderr:
#             st.error(f"Lỗi: {result.stderr}")

#     except Exception as e:
#         st.error(f"Không thể gửi curl: {str(e)}")


# def process_pdf(uploaded_file, scope):
#     if uploaded_file is not None and scope:
#         pdf_bytes = uploaded_file.read()
#         encoded = base64.b64encode(pdf_bytes).decode("utf-8")

#         json_data = {
#             "add": "pdf",
#             "data": encoded,
#             "scope": scope,
#             "filename": uploaded_file.name
#         }
#         save_json(json_data)
#         st.success(f"✅ Đã tạo file g.json với file: `{uploaded_file.name}`")
#         send_curl()
#     else:
#         st.error("❌ Vui lòng chọn file PDF và nhập scope.")


# def process_youtube(url, scope):
#     if url and scope:
#         json_data = {
#             "add": "youtube",
#             "data": url,
#             "scope": scope
#         }
#         save_json(json_data)
#         st.success(f"✅ Đã tạo file g.json cho YouTube URL.")
#         send_curl()
#     else:
#         st.error("❌ Vui lòng nhập đầy đủ URL và scope.")


# def process_search(query, mod, scope):
#     if query and scope:
#         json_data = {
#             "search": query,
#             "mod": mod,
#             "scope": scope
#         }
#         save_json(json_data, filename="h.json")
#         st.success(f"✅ Đã tạo file h.json cho tìm kiếm: `{query}`")
#         send_curl("h.json")
#     else:
#         st.error("❌ Vui lòng nhập đầy đủ nội dung tìm kiếm và scope.")


# def main():
#     st.title("📤 Tìm kiếm bằng từ khóa hoặc ngữ nghĩa")

#     # Sidebar navigation
#     option = st.sidebar.selectbox("Chọn chức năng", (
#         "Gửi PDF", "Gửi YouTube URL", "Tìm kiếm"
#     ))

#     if option == "Gửi PDF":
#         st.header("📝 Thêm PDF vào database")
#         uploaded_file = st.file_uploader("Chọn file PDF", type="pdf")
#         scope = st.text_input("Scope")

#         if st.button("Tạo g.json cho PDF"):
#             process_pdf(uploaded_file, scope)

#     elif option == "Gửi YouTube URL":
#         st.header("📺 Thêm transcript youtube vào database")
#         url = st.text_input("Nhập YouTube URL")
#         scope = st.text_input("Scope")

#         if st.button("Tạo g.json cho URL"):
#             process_youtube(url, scope)

#     elif option == "Tìm kiếm":
#         st.header("🔍 Tìm kiếm")

#         query = st.text_input("Nhập từ khóa tìm kiếm")
#         scope = st.text_input("Scope")
#         mod = st.radio("Chọn phương thức tìm kiếm", ("word", "semantic"))

#         if st.button("Tạo h.json và gửi tìm kiếm"):
#             process_search(query, mod, scope)


# if __name__ == "__main__":
#     main()
import streamlit as st
import base64
import json
import subprocess

# Input for server address with default localhost
server_url = st.sidebar.text_input(
    "Server URL", "http://localhost:8000/",
    help="Nhập địa chỉ server (ví dụ: http://localhost:8000/)"
)


def save_json(data, filename="g.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def send_curl(json_file="g.json"):
    if not server_url.endswith("/"):
        url = server_url + "/"
    else:
        url = server_url

    st.info(f"Đang gửi yêu cầu curl tới {url}")
    try:
        result = subprocess.run(
            [
                "curl", "-s", "-X", "POST",
                "-F", f"file=@{json_file}",
                url
            ],
            capture_output=True,
            text=True
        )
        st.info("📤 Đã gửi yêu cầu curl tới server.")
        # Hiển thị phản hồi
        try:
            parsed = json.loads(result.stdout)
            formatted = json.dumps(parsed, ensure_ascii=False, indent=2)
            st.code(formatted, language="json")
        except json.JSONDecodeError:
            st.code(result.stdout or "Không có phản hồi", language="bash")

        if result.stderr:
            st.error(f"Lỗi: {result.stderr}")

    except Exception as e:
        st.error(f"Không thể gửi curl: {str(e)}")


def process_pdf(uploaded_file, scope, user):
    if uploaded_file is not None and scope and user:
        pdf_bytes = uploaded_file.read()
        encoded = base64.b64encode(pdf_bytes).decode("utf-8")

        json_data = {
            "add": "pdf",
            "data": encoded,
            "scope": scope,
            "filename": uploaded_file.name,
            "user": user
        }
        save_json(json_data)
        st.success(f"✅ Đã tạo file g.json với file: `{uploaded_file.name}` và user: `{user}`")
        send_curl()
    else:
        st.error("❌ Vui lòng chọn file PDF, nhập scope và user.")


def process_youtube(url, scope, user):
    if url and scope and user:
        json_data = {
            "add": "youtube",
            "data": url,
            "scope": scope,
            "user": user
        }
        save_json(json_data)
        st.success(f"✅ Đã tạo file g.json cho YouTube URL và user: `{user}`")
        send_curl()
    else:
        st.error("❌ Vui lòng nhập URL, scope và user.")


def process_search(query, mod, scope, user):
    if query and scope and user:
        json_data = {
            "search": query,
            "mod": mod,
            "scope": scope,
            "user": user
        }
        save_json(json_data, filename="h.json")
        st.success(f"✅ Đã tạo file h.json cho tìm kiếm: `{query}` và user: `{user}`")
        send_curl("h.json")
    else:
        st.error("❌ Vui lòng nhập đầy đủ nội dung tìm kiếm, scope và user.")


def main():
    st.title("📤 Tìm kiếm bằng từ khóa hoặc ngữ nghĩa")

    # Thêm ô nhập user ở cột bên
    user = st.sidebar.text_input("user", help="Nhập tên người dùng để ghi vào JSON")

    # Sidebar navigation
    option = st.sidebar.selectbox("Chọn chức năng", (
        "Gửi PDF", "Gửi YouTube URL", "Tìm kiếm"
    ))

    if option == "Gửi PDF":
        st.header("📝 Thêm PDF vào database")
        uploaded_file = st.file_uploader("Chọn file PDF", type="pdf")
        scope = st.text_input("Scope")

        if st.button("Tạo g.json cho PDF"):
            process_pdf(uploaded_file, scope, user)

    elif option == "Gửi YouTube URL":
        st.header("📺 Thêm transcript YouTube vào database")
        url = st.text_input("Nhập YouTube URL")
        scope = st.text_input("Scope")

        if st.button("Tạo g.json cho URL"):
            process_youtube(url, scope, user)

    elif option == "Tìm kiếm":
        st.header("🔍 Tìm kiếm")

        query = st.text_input("Nhập từ khóa tìm kiếm")
        scope = st.text_input("Scope")
        mod = st.radio("Chọn phương thức tìm kiếm", ("word", "semantic"))

        if st.button("Tạo h.json và gửi tìm kiếm"):
            process_search(query, mod, scope, user)


if __name__ == "__main__":
    main()
