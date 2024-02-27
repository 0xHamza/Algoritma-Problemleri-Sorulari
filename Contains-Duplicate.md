## Giriş

Bu depolama alanı, C# dilinde "Contains Duplicate" problemini çözmek için çeşitli yaklaşımları incelemektedir. Problem, bir dizinin herhangi bir yinelenen öğe içerip içermediğini belirlemeyi içerir.
[LeetCode Contains Duplicate](https://leetcode.com/problems/contains-duplicate)

1. Brute Force (Kaba Kuvvet) Çözümü: İki katmanlı bir döngü kullanarak her bir sayıyı diğer tüm sayılarla karşılaştırma. Eğer aynı sayı birden fazla kez bulunursa, true döndürülür. Aksi halde, false döndürülür.
2. HashSet (Küme) Çözümü: Bir HashSet veri yapısı kullanılarak her bir sayının bir kere görülüp görülmediği kontrol edilir. Eğer bir sayı daha önce set içinde bulunuyorsa, true döndürülür. Aksi halde, sete eklenir ve işlem devam eder.
3. HashMap (Sözlük) Çözümü: Bir Dictionary (sözlük) veri yapısı kullanılarak her bir sayının bir kere görülüp görülmediği kontrol edilir. Eğer bir sayı daha önce sözlük içinde bulunuyorsa, true döndürülür. Aksi halde, sözlüğe eklenir ve işlem devam eder.
4. Sıralı (Sorted) Çözümü: Dizi sıralandıktan sonra, ardışık elemanlar arasında tekrar eden bir sayı olup olmadığı kontrol edilir. Eğer bir sayı, bir sonraki sayı ile aynıysa, true döndürülür. Aksi halde, false döndürülür.
5. HashSet (Küme) ile ToHashSet Kullanımı: C# dilinde sunulan ToHashSet() fonksiyonu kullanılarak dizi bir küme veri yapısına dönüştürülür ve dizide tekrar eden bir sayı olup olmadığı kontrol edilir.

## Çözümler

1. Brute Force

```C#
public bool ContainsDuplicate(int[] nums) {
    for(int i = 0; i<nums.Length; i++)
        for(int j = i+1; j<nums.Length; j++)
            if(nums[i] == nums[j])
                return true;
    return false;
}

// Zaman Karmaşıklığı: O(n^2)
```
Bu çözüm, her bir öğeyi diğer tüm öğelerle karşılaştırarak yinelenen öğeleri arar. Bu basit bir çözümdür, ancak büyük diziler için zaman alıcı olabilir.

2. HashSet

```C#
public bool ContainsDuplicate(int[] nums) {
    HashSet<int> hash = new HashSet<int>();
        
    foreach(int num in nums){
        if(hash.Contains(num))
            return true;

        hash.Add(num);
    }
    return false;
}

// Zaman Karmaşıklığı: O(n)
```
Bu çözüm, yinelenen öğeleri bulmak için bir HashSet kullanır. HashSet'te bir öğe eklemek veya aramak sabit bir sürede gerçekleşir, bu da bu çözümü büyük diziler için daha hızlı hale getirir.

3. HashMap

```C#
public bool ContainsDuplicate(int[] nums) {
    Dictionary<int, int> map = new Dictionary<int, int>();
    foreach (int num in nums) {
        if (map.ContainsKey(num)) {
            return true;
        }
        map[num] = 1;
    }
    return false;
}

// Zaman Karmaşıklığı: O(n)
```
Bu çözüm, yinelenen öğeleri bulmak için bir HashMap kullanır. HashMap'te bir öğe eklemek veya aramak sabit bir sürede gerçekleşir, bu da bu çözümü büyük diziler için daha hızlı hale getirir.

4. Sıralama

```C#
public bool ContainsDuplicate(int[] nums) {
    Array.Sort(nums);
    for (int i = 1; i < nums.Length; i++)
        if (nums[i] == nums[i - 1])
            return true;
    return false;
}

// Zaman Karmaşıklığı: O(n log n)
```
Bu çözüm, dizideki öğeleri sıralamak için Array.Sort yöntemini kullanır ve ardından ardışık öğeleri karşılaştırarak yinelenen öğeleri arar. Sıralama işleminin zaman karmaşıklığı O(n log n)'dir, bu da diğer çözümlerden daha yavaş olabilir.


| Çözüm     |	Zaman Karmaşıklığı |	Avantajlar	| Dezavantajlar |
|---|---|---|---|
| Brute Force |	O(n^2) |	Basit |	Büyük diziler için zaman alıcı |
| HashSet	| O(n)	| Hızlı	|Ek bellek kullanımı |
| HashMap	| O(n)	| Hızlı	|Ek bellek kullanımı |
| Sıralama |	O(n log n)	| Dizideki öğelerin sırasını da verir |	Sıralama işlemi zaman alıcı olabilir |
