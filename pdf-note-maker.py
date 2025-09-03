import fitz
import sys
import os
import re

def create_pdf_with_notes(input_path, output_path, note_type='grid', content_ratio=3, notes_ratio=2):

    try:
        if os.path.getsize(input_path) == 0:
            print(f"\n⚠️ 경고: '{os.path.basename(input_path)}' 파일이 비어있어 건너뜁니다.")
            return

        doc = fitz.open(input_path)
        new_doc = fitz.open()

        if not doc:
            print(f"\n⚠️ 경고: '{os.path.basename(input_path)}' 파일에 페이지가 없어 건너뜁니다.")
            return
            
        original_width = doc[0].rect.width
        original_height = doc[0].rect.height
        
        margin = 5.0
        
        usable_width = original_width - (margin * 2)
        usable_height = original_height - (margin * 2)
        
        total_ratio = content_ratio + notes_ratio
        content_width = usable_width * (content_ratio / total_ratio)
        
        total_new_pages = (len(doc) + 1) // 2
        
        for i in range(0, len(doc), 2):
            new_page = new_doc.new_page(width=original_width, height=original_height)
            
            if i < len(doc):
                pix = doc[i].get_pixmap(dpi=300)
                target_rect_top = fitz.Rect(margin, margin, margin + content_width, margin + usable_height / 2)
                new_page.insert_image(target_rect_top, pixmap=pix)
            
            if i + 1 < len(doc):
                pix = doc[i + 1].get_pixmap(dpi=300)
                target_rect_bottom = fitz.Rect(margin, margin + usable_height / 2, margin + content_width, original_height - margin)
                new_page.insert_image(target_rect_bottom, pixmap=pix)

            notes_start_x = margin + content_width + 10
            notes_end_x = original_width - margin
            
            separator_x = margin + content_width + 5
            p1 = fitz.Point(separator_x, margin)
            p2 = fitz.Point(separator_x, original_height - margin)
            new_page.draw_line(p1, p2, color=(0.8, 0.8, 0.8), width=0.5)

            line_color = (0.85, 0.85, 0.85)
            
            if note_type == 'grid':
                gap = 12
            else: # line
                gap = 20

            current_y = margin + gap
            while current_y < (original_height - margin):
                p_start = fitz.Point(notes_start_x, current_y)
                p_end = fitz.Point(notes_end_x, current_y)
                new_page.draw_line(p_start, p_end, color=line_color, width=0.5)
                current_y += gap

            if note_type == 'grid':
                current_x = notes_start_x
                # --- 변경 끝 ---
                while current_x < notes_end_x:
                    p_start = fitz.Point(current_x, margin)
                    p_end = fitz.Point(current_x, original_height - margin)
                    new_page.draw_line(p_start, p_end, color=line_color, width=0.5)
                    current_x += gap

            current_page_num = (i // 2) + 1
            page_text = f"{current_page_num} / {total_new_pages}"
            
            text_box = fitz.Rect(original_width - margin - 50, original_height - margin - 15, original_width - margin, original_height - margin)
            
            new_page.insert_textbox(text_box, page_text, fontsize=8, fontname="helv", color=(0.6, 0.6, 0.6), align=fitz.TEXT_ALIGN_RIGHT)

        new_doc.save(output_path, garbage=4, deflate=True)
        new_doc.close()
        doc.close()
        print(f"✅ '{os.path.basename(output_path)}' 생성 완료!")

    except Exception as e:
        print(f"\n❌ 오류 발생 ({os.path.basename(input_path)}): {e}")

if __name__ == "__main__":
    print("-" * 50)
    print("PDF를 필기 노트로 바꿔봅시다.(모눈/라인 선택)")
    print("-" * 50)

    LEFT_RATIO = 5
    RIGHT_RATIO = 3

    note_choice = ''
    while note_choice not in ['1', '2']:
        note_choice = input("원하는 필기 노트 스타일을 선택하세요:\n  1. 모눈 \n  2. 라인 \n> ")

    note_style = 'grid' if note_choice == '1' else 'line'
    
    input_text = input("\n처리할 PDF 파일들을 드래그하거나, 경로를 쉼표(,)로 구분해 입력하세요:\n> ")
    
    if '"' in input_text:
        input_files = re.findall(r'\"(.*?)\"|(\S+)', input_text)
        input_files = [path[0] if path[0] else path[1] for path in input_files]
    else:
        input_files = input_text.replace(',', ' ').split()

    print(f"\n총 {len(input_files)}개의 파일을 '{note_style}' 스타일로 처리합니다...")
    
    successful_count = 0
    for file_path in input_files:
        clean_path = file_path.strip().strip('"')

        if not os.path.exists(clean_path):
            print(f"❌ 오류: '{clean_path}' 파일을 찾을 수 없습니다.")
            continue
        elif not clean_path.lower().endswith('.pdf'):
            print(f"❌ 오류: '{clean_path}'는 PDF 파일이 아닙니다.")
            continue
        
        base, ext = os.path.splitext(clean_path)
        output_file = f"{base}_필기용_{'모눈' if note_style == 'grid' else '라인'}{ext}"
        
        print(f"\n- '{os.path.basename(clean_path)}' 변환 중...")
        create_pdf_with_notes(clean_path, output_file, note_type=note_style, content_ratio=LEFT_RATIO, notes_ratio=RIGHT_RATIO)
        successful_count += 1
        
    print(f"\n--- 작업 완료 ---")
    print(f"총 {len(input_files)}개 중 {successful_count}개 파일 변환 성공!")
    input("창을 닫으려면 엔터를 누르세요...")
