``` cpp
#include <iostream>
#include <string>

using namespace std;

class Weapon {
public:
    Weapon(string name, int damage) {
        this->name = name;
        this->damage = damage;
    }
    string getName() {
        return name;
    }
    int getDamage() {
        return damage;
    }
private:
    string name;
    int damage;
};
```

# Call by reference
인자를 참조(reference)로 전달하는 방식입니다. 함수 호출 시 인자로 전달된 변수의 메모리 주소를 전달하여 함수 내에서 해당 변수를 직접 참조할 수 있습니다. 따라서 함수 내에서 해당 변수의 값을 변경하면 호출된 곳에서도 변경된 값을 사용할 수 있습니다.


``` cpp
void attackByReference(Weapon& weaponRef) {
cout << "공격: " << weaponRef.getName() << " (데미지: " << weaponRef.getDamage() << ")" << endl;
// 무기의 소모품질을 1 감소시킴
weaponRef.use();
}

int main() {
Weapon mySword("마법검", 10, 100); // 이름: 마법검, 데미지: 10, 내구도: 100
attackByReference(mySword); // 무기의 이름, 데미지 출력, 내구도 1 감소
cout << "남은 내구도: " << mySword.getDurability() << endl; // 99 출력
return 0;
}

```

## 결과
``` cpp
// 공격: 마법검 (데미지: 10)
// 남은 내구도: 99
```

# Call by address
인자를 포인터(pointer)로 전달하는 방식입니다. 함수 호출 시 인자로 전달된 변수의 메모리 주소를 전달하여 함수 내에서 해당 변수를 간접적으로 참조할 수 있습니다. 따라서 함수 내에서 해당 변수의 값을 변경하면 호출된 곳에서도 변경된 값을 사용할 수 있습니다.

``` cpp
void attackByAddress(Weapon* weaponPtr) {
    cout << "공격: " << weaponPtr->getName() << " (데미지: " << weaponPtr->getDamage() << ")" << endl;
    // 무기의 소모품질을 감소시키기
    weaponPtr->setDurability(weaponPtr->getDurability() - 1);
}

int main() {
    Weapon weapon("검", 10, 100);
    attackByAddress(&weapon);
    cout << "무기 소모품질: " << weapon.getDurability() << endl;
    return 0;
}


```

## 결과
``` cpp
// 공격: 검 (데미지: 10)
// 무기 소모품질: 99
```

# Call by value
인자를 값(value)으로 전달하는 방식입니다. 함수 호출 시 인자로 전달된 변수의 값을 복사하여 전달하며, 함수 내에서 해당 변수의 값을 변경하더라도 호출된 곳에서는 영향을 받지 않습니다.

``` cpp
void attackByValue(Weapon weapon) {
    cout << "공격: " << weapon.getName() << " (데미지: " << weapon.getDamage() << ")" << endl;
    // 무기의 소모품질을 감소시키기
    weapon.setDurability(weapon.getDurability() - 1);
}

int main() {
    Weapon weapon("검", 10, 100);
    attackByValue(weapon);
    cout << "무기 소모품질: " << weapon.getDurability() << endl;
    return 0;
}

```
## 결과

``` cpp
// 공격: 검 (데미지: 10)
// 무기 소모품질: 100
```

