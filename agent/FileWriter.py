from I_Writer import Writer
from datetime import datetime
import json


class FileWriterWithTime(Writer):
    """
    כתיבת הנתונים לקובץ בפןרמט {json},
     תוך הוספת תאריך ושעה לכל כתיבה,
    הנתונים צריכים להיות מסוג {str}
    """

    def send_data(self, file_name: str) -> None:
        """כתיבה לקובץ בפורמט {json} בתוספת זמן"""
        if (self.data is None) or (not isinstance(self.data, str)):
            raise ValueError('The data was not received or is not of type string.')
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        data_with_time = {current_time: self.data}
        json_data = json.dumps(data_with_time, ensure_ascii=False)
        try:
            with open(file_name, 'a', encoding='utf-8') as file:
                file.write(json_data + '\n')
        except Exception as e:
            print(f'error: {e}')

# הושלם