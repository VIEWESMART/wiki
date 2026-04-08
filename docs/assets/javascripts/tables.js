document$.subscribe(function() {
  // 选择所有没有 class 的表格
  var tables = document.querySelectorAll("article table:not([class])");

  // 遍历表格
  tables.forEach(function(table) {
    // 1. 获取表格数据行的数量 (只计算 tbody 里的 tr，排除表头)
    var rowCount = table.querySelectorAll("tbody tr").length;

    // 2. 判断是否超过 5 行
    var showSearch = rowCount > 5;

    // 3. 初始化 DataTables
    $(table).DataTable({
      "paging": false,
      "info": false,
      "searching": showSearch, // <--- 关键修改：这里使用变量控制
      "ordering": true,
      "scrollX": true,
      "autoWidth": false,
      "language": {
        "search": "🔍 Filter:",
        "searchPlaceholder": "Search SKU..."
      }
    });
  });
});