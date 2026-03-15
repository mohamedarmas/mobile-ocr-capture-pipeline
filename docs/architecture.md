            +----------------------+
            |   Android Device     |
            |   (ADB Capture)      |
            +----------+-----------+
                       |
                       v
               capture_android_screen()
                       |
                       v
                 PNG Screenshot
                       |
                       v
            +----------------------+
            | Azure Document AI    |
            | prebuilt-read model  |
            +----------+-----------+
                       |
                       v
              extract_text_from_image()
                       |
                       v
                  Structured Text
                       |
                       v
                JSON / CSV Output