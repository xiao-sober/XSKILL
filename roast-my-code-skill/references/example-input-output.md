# Example Input And Output

Use this reference to keep future outputs both funny and useful.

## Example User Request

> 吐槽一下这段代码，但要能让我知道怎么改。

```js
function getUserData(id, users) {
  let result = null;
  for (let i = 0; i < users.length; i++) {
    if (users[i].id == id) {
      result = users[i];
    }
  }
  if (result == null) {
    console.log("no user");
  }
  return result.name;
}
```

## Example Output

## 总体印象

这段函数看起来想找用户，但它对失败路径的尊重程度基本等于没有。

## 最值得吐槽的 3~5 点

### 1. 找不到用户还硬拿 `name` `[severity: high]` `[type: true issue]`

- 问题说明：`result` 可能保持 `null`，但函数最后仍然执行 `return result.name`。
- 为什么值得吐槽：前面刚刚 `console.log("no user")`，下一秒就开始访问 `null.name`，这属于一边报警一边继续往坑里走。
- 可能影响：当用户不存在时会抛出运行时错误，调用方拿不到稳定的失败结果。
- 建议改法：找不到用户时直接返回 `null`、抛出明确错误，或返回统一的结果对象。

```js
if (!result) {
  return null;
}
return result.name;
```

### 2. `==` 让 ID 匹配进入玄学模式 `[severity: medium]` `[type: true issue]`

- 问题说明：`users[i].id == id` 会进行隐式类型转换。
- 为什么值得吐槽：`"1"` 和 `1` 可能被当成同一个用户，除非这就是业务设定，否则这段代码是在替产品经理偷偷做决定。
- 可能影响：ID 类型不一致时可能匹配到不该匹配的数据。
- 建议改法：明确 ID 类型，并使用 `===`。如果外部输入可能是字符串，先在边界处统一转换。

### 3. 找到以后还继续循环 `[severity: low]` `[type: true issue]`

- 问题说明：找到匹配用户后没有 `break` 或提前 `return`。
- 为什么值得吐槽：函数已经找到人了，还继续在人群里喊名字，效率和场面都不太优雅。
- 可能影响：小数组影响不大；大数组会浪费时间。如果存在重复 ID，后面的结果还会覆盖前面的结果。
- 建议改法：用 `find` 表达意图，或者找到后立刻返回。

```js
const user = users.find((user) => user.id === id);
return user ? user.name : null;
```

## 真正严重的问题

- 找不到用户时访问 `result.name` 会导致运行时错误。

## 其实还不错的地方

- 函数意图是清楚的：按 ID 从用户列表里取名称。
- 没有把查找逻辑和外部 API 调用混在一起，局部修改成本不高。

## 一句话总结

这段代码离可用不远，但失败路径现在像没装护栏的楼梯，先把不存在用户的返回契约补上。

## Notes

This example is intentionally short. In real reviews:

- Cite file paths and line numbers when available.
- Preserve the user's language.
- Use fewer jokes in high-risk or formal contexts.
- Include tests or test suggestions when the issue is behavioral.
