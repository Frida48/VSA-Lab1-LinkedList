VSA1 - Laboratoriya İşi 1

Tələbə: Fəridə Mikayılzadə
Group: KOM25

İşin Adı : Linked Lists (Bağlı Siyahılar)

Yerinə Yetirilmiş Tapşırıqlar:
Aşağıdakı əməliyyatlar kodda uğurla yerinə yetirilmişdir:
- Insert at beginning (Əvvələ element əlavə etmək)
- Insert at end (Sona element əlavə etmək)
- Delete node (Verilmiş node-u silmək)
- Search node (Node axtarışı etmək)
- Reverse list (Siyahını tərsinə çevirmək)

## Proqramın İş Prinsipi
Proqramda Linked List (Bağlı Siyahı) strukturu yaradılmışdır. Hər bir element (Node) özündə məlumat (data) və növbəti elementin ünvanını (pointer) saxlayır. Siyahının başlanğıcı head göstəricisi ilə təyin olunur. Bütün əməliyyatlar bu head-dən başlayaraq while dövrləri vasitəsilə icra olunur. Yeni elementlər əlavə edilərkən və ya silinərkən next göstəriciləri yenidən təyin edilir ki, siyahının bütövlüyü pozulmasın.

## İcra Təlimatı
Kodu işə salmaq üçün terminalda scr qovluğuna daxil olub aşağıdakı əmri yazmaq kifayətdir:

```bash
python linkedlist.py
