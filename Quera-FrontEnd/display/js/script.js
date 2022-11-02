$(document).ready(() => {

    function dropDownEvent(){
        
        function update(btn, isDisplay){
            const menu  = $(btn.parents("div.dropdown")[0]);
            const show  = $(menu.children('button')[0])
            const value = btn.html();
            const key   = btn.attr("value")? btn.attr("value"):"display";
            show.html(value);
            $(".my_container").css(key, value);
            if (isDisplay)
                updateOptions(value);
        }

        function click(event, isDisplay=true){
            const btn = $(event.target);
            update(btn, isDisplay);
        }

        function updateOptions(value){
            const option = $("#options-col");
            if (value == "flex"){
                const options = {
                    "flex-direction": [
                        "row",
                        "row-reverse",
                        "column",
                        "column-reverse"
                    ],
                    "flex-wrap": [
                        "no-wrap",
                        "wrap",
                        "wrap-reverse"
                    ],
                    "justify-content": [
                        "flex-start",
                        "flex-end",
                        "center",
                        "space-between",
                        "space-arround",
                        "space-evenly",
                    ],
                    "align-items": [
                        "scretch",
                        "flex-start",
                        "flex-end",
                        "center",
                        "baseline",
                    ]
                };
                const items = Object.keys(options).map(key => {
                    const values    = options[key];
                    const list      = `
                    <ul class="dropdown-menu" aria-labelledby="${key}">
                        ${values.map(v => {
                            return `
                            <li>
                                <a class="dropdown-item option-item" value="${key}">
                                    ${v}
                                </a>
                            </li>
                            `
                        }).join('')}
                    </ul>
                    `;  
                    const dropdown  = `
                    <div class="h4 text-center"> ${key}</div>
                    <div class="dropdown my-3 center-block">
                        
                        <button class="btn btn-primary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="${key}">
                            ${$(".my_container").css(key)}
                        </button>
                        ${list}
                    </div>`;
                    return dropdown;
                }).join('');
                option.html(items);
                $(".option-item").click(e => click(e, false));
            } else {
                option.html(`<h3 class="text-center"> no option </h3>`);
            }
        }

        $(".dropdown-item").click(e => click(e));
    }

    function setupPage(){
        dropDownEvent();
    }

    setupPage();
});
